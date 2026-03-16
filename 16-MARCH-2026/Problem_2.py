from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")

sleep(2)

print("Title:", driver.title)

yes_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
yes_button.click()

result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result Message:", result.text)

print("Class:", yes_button.get_attribute("class"))
print("ID:", yes_button.get_attribute("for"))

print("Current URL:", driver.current_url)

sleep(5)

driver.quit()