from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

sleep(2)


print("Title:", driver.title)

username = driver.find_element(By.NAME, "username")
username.clear()

username.send_keys("Admin")

password = driver.find_element(By.NAME, "password")
password.send_keys("admin123")

login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()

sleep(3)

current_url = driver.current_url
print("Current URL:", current_url)

# 8. Check if dashboard is present in URL
if "dashboard" in current_url:
    print("successful login")

sleep(5)
driver.quit()