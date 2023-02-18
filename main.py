import requests
from bs4 import BeautifulSoup
import smtplib

# Define the URL of the Adafruit Raspberry Pi product page
url = 'https://www.adafruit.com/product/3775'

# Send a request to the website and get the HTML content
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the availability message on the page
availability_div = soup.find('div', {'class': 'purchase-info-message'})
if availability_div is not None:
    availability = availability_div.text.strip()
    # Check if the Raspberry Pi is in stock
    if availability == 'IN STOCK':
        # If the Raspberry Pi is in stock, send an email notification
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_email_password')
        message = 'The Raspberry Pi is in stock on Adafruit!'
        server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', message)
        server.quit()
