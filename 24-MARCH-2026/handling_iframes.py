from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
#
# # simple  iframe
# iframe=driver.find_element(By.ID,'singleframe')
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')


# nested iframe
driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()

nested_iframe=driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)

inner_iframe=driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(2)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('123')


sleep(2)
driver.quit()