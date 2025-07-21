
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")

# Wait for QR code scan
print("Scan the QR code with your phone to log in to WhatsApp Web")
time.sleep(20)  # Wait for user to scan QR code (increase if needed)

# Name or number you saved yourself as (e.g., "Myself")
your_contact_name = "You"

# Search and click on the chat
search_box = driver.find_element(By.XPATH, '//div[@title="Search input textbox"]')
search_box.click()
search_box.send_keys(your_contact_name)
time.sleep(2)

# Select chat
contact = driver.find_element(By.XPATH, f'//span[@title="{your_contact_name}"]')
contact.click()

# Message you want to send
message = "Hello from Python bot using Selenium!"

# Find message input box and send message
message_box = driver.find_element(By.XPATH, '//div[@title="Type a message"]')
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)

print("Message sent successfully!")
time.sleep(5)
driver.quit()
