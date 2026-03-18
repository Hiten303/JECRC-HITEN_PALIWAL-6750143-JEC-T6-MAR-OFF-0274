
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
sleep(3)

chose_file= driver.find_element(By.ID,"file-upload")
chose_file.send_keys("C:\Users\user\OneDrive\Downloads\ChatGPT Image Mar 13, 2026, 09_05_38 PM.png")
