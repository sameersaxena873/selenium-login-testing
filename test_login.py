from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Browser open karo
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# ---------- TEST CASE 1: Valid Login ----------
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
time.sleep(2)

message1 = driver.find_element(By.ID, "flash").text
print("Test Case 1 (Valid Login) Result:", message1)

# ---------- Reset session before Test Case 2 ----------
driver.delete_all_cookies()
time.sleep(1)

# ---------- TEST CASE 2: Invalid Login ----------
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

username2 = driver.find_element(By.ID, "username")
password2 = driver.find_element(By.ID, "password")

username2.send_keys("wronguser")
password2.send_keys("wrongpassword")

login_button2 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button2.click()
time.sleep(2)

message2 = driver.find_element(By.ID, "flash").text
print("Test Case 2 (Invalid Login) Result:", message2)

time.sleep(3)
driver.quit()