from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('Detach', True)
# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# sleep(3)
# action=ActionChains(driver)
#
# origin_ele=driver.find_element(By.ID,'column-a')
# target_ele=driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
#
# sleep(3)

# driver = webdriver.Chrome()
# driver.get('https://supertails.com/')
#
# action=ActionChains(driver)
# element=driver.find_element(By.XPATH,'//span[contains(text(),"Dogs")][1]')
# action.move_to_element(element).perform()
# sleep(2)
#
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/droppable')
# sleep(3)
# action=ActionChains(driver)
#
# for i in range(5):
#
#      origin_ele=driver.find_element(By.ID,'draggable')
#      target_ele=driver.find_element(By.ID,'droppable')
#
#      action.drag_and_drop(origin_ele,target_ele).perform()
#
#      assert "Dropped!" in target_ele.text ,'Failed'
#      driver.refresh()


driver = webdriver.Chrome()
driver.get('https://supertails.com/')


cat=driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
action=ActionChains(driver)
# action.scroll_to_element(cat).perform()
action.scroll_by_amount(0,-1500).perform()
# action.scroll_from_origin(0,0,1000).perform()

sleep(3)
driver.quit()