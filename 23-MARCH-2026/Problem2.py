from prompt_toolkit.contrib.telnet.protocol import EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.myntra.com/')
action=ActionChains(driver)
wait = WebDriverWait(driver, 10)
men=driver.find_element(By.XPATH,'//a[@data-group="men"]')
action.move_to_element(men).perform()
footware=wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@data-reactid="90"]')))
footware.click()
sleep(2)
action.scroll_by_amount(0,1500).perform()

sleep(3)
driver.quit()