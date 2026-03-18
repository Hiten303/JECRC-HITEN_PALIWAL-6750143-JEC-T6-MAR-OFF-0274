
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.lenskart.com/eyeglasses/marketing/bestsellers-premium-eyeglasses.html?dir=desc&gan_data=true&sort=created")

sleep(2)

sort=driver.find_element(By.ID,'sortByDropdown')
dropdown=Select(sort)
dropdown.select_by_value("saving")
sleep(2)


new_result = driver.find_element(By.XPATH, "(//div[@class='sc-bf32d8a7-0 gOVKHN']/div)")

print(new_result.text)

sleep(2)

driver.quit()

