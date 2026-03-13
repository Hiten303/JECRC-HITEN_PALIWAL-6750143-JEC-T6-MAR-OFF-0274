'''
ChromeOptions used to customize the browser launching
'''
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
opts=webdriver.ChromeOptions()
# opts.add_argument('--headless')
opts.add_experimental_option('detach', True)
driver=webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
sleep(3)
print('it is working fine')
# driver.find_element('id')

print('finding element by id')
name=driver.find_element(By.ID,'name')
phone=driver.find_element(By.ID,'phone')
email=driver.find_element(By.ID,'email')
textarea=driver.find_element(By.ID,'textarea')
country=driver.find_element(By.ID,'country')

print(name)
print(phone)
print(email)
print(textarea)
print(country)

print('finding element by name')
nav_bar=driver.find_element(By.NAME,'Navbar')
header=driver.find_element(By.NAME,'Header')
main=driver.find_element(By.NAME,'Main')
cross_column=driver.find_element(By.NAME,'Cross-Column')
gender=driver.find_element(By.NAME,'gender')
print(nav_bar)
print(header)
print(main)
print(cross_column)
print(gender)

print('finding element by classname')
radio=driver.find_elements(By.CLASS_NAME,'form-check-input')

print('finding element using css selector')
animals=driver.find_element(By.CSS_SELECTOR,'#animals')
links=driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
placeholders=driver.find_element(By.XPATH,'//input[@placeholder="Enter Name"]')
home=driver.find_element(By.XPATH,'//a[text()="Home"]')

print(animals)
print(links)
print(placeholders)
for i in range(5):
    print(radio[i])


print('done')
