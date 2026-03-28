from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
wait=WebDriverWait(driver,10)

alert1=driver.find_element(By.XPATH,'//button[@id="alertButton"]').click()
driver.switch_to.alert.accept()
#
driver.find_element(By.XPATH,'//button[@id="timerAlertButton"]').click()
wait.until(EC.alert_is_present()).accept()
sleep(3)

driver.find_element(By.XPATH,'//button[@id="confirmButton"]').click()
alert3=wait.until(EC.alert_is_present())
alert3.accept()
text = driver.find_element(By.ID, "confirmResult").text
assert "You selected Ok" in text
sleep(3)

driver.find_element(By.XPATH,'//button[@id="promtButton"]').click()
alert4=wait.until(EC.alert_is_present())
alert4.send_keys('hiten paliwal')
alert4.accept()


text = driver.find_element(By.ID, "promptResult").text

assert "hiten paliwal" in text

sleep(3)
driver.quit()
