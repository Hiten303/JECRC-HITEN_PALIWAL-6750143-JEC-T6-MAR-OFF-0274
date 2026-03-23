from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)


driver.get(r'D:\pycharm\project\23-MARCH-2026\form.html')
action=ActionChains(driver)
present_address=driver.find_element(By.ID,'presentAddress')
permanent_address=driver.find_element(By.ID,'permanentAddress')

sleep(3)
present_address.send_keys('40, Karm sheel marg, outside chandpole udaipur rajasthan')
sleep(3)

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
sleep(3)

action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
permanent_address.click()
sleep(3)

action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

sleep(3)
driver.quit()