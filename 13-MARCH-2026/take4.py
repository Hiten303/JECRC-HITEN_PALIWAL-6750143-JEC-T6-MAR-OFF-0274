from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

time.sleep(3)   # give page time to load

#  Search bar
search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print("Search bar found")

#  Amazon logo
logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print("Logo found")

# Cart icon
cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print("Cart found")

#  Sign in link
sign_in = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print("Sign in found")

# Category links
categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")

print("Total categories:", len(categories))

for c in categories:
    print(c.text)

driver.quit()