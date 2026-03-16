from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# sleep(2)
# driver.get("https://www.cricbuzz.com")
# sleep(2)
driver.get("https://www.amazon.in")
sleep(2)



element=driver.find_element(By.XPATH,'//span[text()="All"]/ancestor::div[@id="nav-main"]')
print('found the first element')
element2=driver.find_element(By.XPATH,'//div[@id="nav-main"]/descendant::span[text()="All"]')
print('found the second element')
# //a[text()="Fresh"]/ancestor::li/following-sibling::li[1]
linktexts=driver.find_element(By.LINK_TEXT,'').text

driver.find_element(By.LINK_TEXT,"Udemy Courses")
driver.find_element(By.PARTIAL_LINK_TEXT,"Udemy")
element2.click()
sleep(2)
print(element.get_attribute('class'))
driver.quit()