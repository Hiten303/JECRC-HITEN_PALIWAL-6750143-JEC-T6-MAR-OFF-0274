from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/windows')
#
# parent_window=driver.current_window_handle
#
# driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# sleep(2)
# all_windows = driver.window_handles
# print(len(all_windows))
# driver.switch_to.window(all_windows[-1])
# print(driver.find_element(By.CLASS_NAME,'example').text)
# assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
#
# driver.switch_to.window(parent_window)

# opening a website in new window
driver.get("https://google.com")
sleep(3)
driver.switch_to.new_window('tab')
sleep(3)
driver.get('https://monkeytype.com/')


sleep(3)
driver.quit()