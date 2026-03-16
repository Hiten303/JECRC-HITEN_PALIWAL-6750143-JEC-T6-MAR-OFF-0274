from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opt)

driver.get("https://www.amazon.in/")
sleep(5)

search=driver.find_element(By.ID,'twotabsearchtextbox')
search.clear()
# search.send_keys('mobile')
# button=driver.find_element(By.ID,'nav-search-submit-button')
# button.click()
search.send_keys('mobile',Keys.ENTER)

# filters=driver.find_element(By.ID,'s-all-filters-announce')
# filters.click()

brands=driver.find_element(By.XPATH,'//*[@id="p_123/46655"]/span/a/div/label/i')
brands.click()





sleep(3)
driver.quit()






