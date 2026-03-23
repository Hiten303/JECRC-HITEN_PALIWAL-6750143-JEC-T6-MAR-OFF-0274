from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.royalchallengers.com/')
action=ActionChains(driver)
image=driver.find_element(By.XPATH,'(//span[@class="prod-img"]/img)[6]')
action.scroll_to_element(image).perform()
sleep(3)

for i in range(5):
    print('hello')
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(2)
sleep(3)
driver.quit()
