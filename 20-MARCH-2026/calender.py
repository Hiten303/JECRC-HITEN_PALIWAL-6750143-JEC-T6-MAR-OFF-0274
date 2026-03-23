from time import sleep
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.Id,'datepicker').send_keys("30/03/2004",Keys.ENTER)
month=('May')
date='2'


driver.find_element(By.ID,'txtDate').click()
sleep(3)
select = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
select.select_by_visible_text(month)
driver.find_element(By.XPATH,f'//a[text()={date}]/parent::td').click()

sleep(3)
driver.quit()