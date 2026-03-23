from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get(r'D:\pycharm\project\23-MARCH-2026\index1.html')
action=ActionChains(driver)


driver.find_element(By.ID,'password').send_keys('hit')
sleep(3)
show=driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show).perform()
sleep(4)
action.release().perform()
sleep(2)
driver.quit()
