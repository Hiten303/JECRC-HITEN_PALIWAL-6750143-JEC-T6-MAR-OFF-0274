import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

folder=os.path.join(os.getcwd(),'screenshots')
os.makedirs(folder,exist_ok=True)
driver = webdriver.Chrome()
action = ActionChains(driver)
driver.get("https://in.pinterest.com/")
sleep(3)
driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)

# ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
ele=driver.find_element(By.XPATH,'//img[contains(@alt,"Photo of a woman in a cherry-patterned sweater vest, white shirt, blue")]')

action.scroll_to_element(ele).perform()
sleep(3)

ele.screenshot(f'{folder}/girl.png')
driver.quit()
