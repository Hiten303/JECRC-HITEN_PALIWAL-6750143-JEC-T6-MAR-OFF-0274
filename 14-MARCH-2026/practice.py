from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://cricbuzz.com/')
sleep(3)
element=driver.find_element(By.XPATH,'//*[@class="shadow rounded-md overflow-hidden"]')
element.click()
summary=driver.find_element(By.XPATH,'//*[@class="text-cbTextLink"]')
print(summary.text)