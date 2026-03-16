from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(3)
price = driver.find_element(By.XPATH,'//td[text()="Learn Java"]/following-sibling::td[3]')
print(price.text)
subject=driver.find_element(By.XPATH,'//td[text()="Amod"]/ancestor::tbody/tr[2]/td[3]')
print(subject.text)
bookname=driver.find_elements(By.XPATH,'//tr[td[4]="300"]/td[1]')
for i in bookname:
    print(i.text)

driver.quit()

