from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')


# simple alert
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.accept()

# confirmation alert
driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.dismiss()

# prompt alert
driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
sleep(3)
alert=driver.switch_to.alert
alert.send_keys('hello world')
sleep(3)
alert.accept()


# switching to alert using wait
wait=WebDriverWait(driver,10)
alert=wait.until(EC.alert_is_present())
sleep(3)
alert.accept()


sleep(3)
driver.quit()