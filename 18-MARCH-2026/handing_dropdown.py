

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

country=driver.find_element(By.ID,'country')
dropdown=Select(country)
dropdown.select_by_value('india')
sleep(2)
dropdown.select_by_index(3)
sleep(5)