from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')



driver.find_element(By.ID, "username").send_keys("Hiten")
sleep(1)



driver.find_element(By.ID, "email").send_keys("hitenpaliwal097@gmail.com")
sleep(1)

# driver.find_element(By.XPATH, "//label[text()='Male']").click()
# sleep(1)

driver.find_element(By.ID, "tel").send_keys("1234567890")
sleep(1)
#
# driver.find_element(By.ID, "fax").send_keys("67890")
# sleep(1)

# subjects = driver.find_element(By.ID, "subjectsInput")
# subjects.send_keys("Maths")
# subjects.send_keys(Keys.ENTER)
# sleep(1)
# subjects.send_keys("Physics")
# subjects.send_keys(Keys.ENTER)
# sleep(1)
#
# driver.find_element(By.XPATH, "//label[text()='Sports']").click()
# driver.find_element(By.XPATH, "//label[text()='Music']").click()
# sleep(1)

driver.find_element(By.XPATH, '//*[@id="container"]/div[6]/input').send_keys(r"C:\Users\user\OneDrive\Documents\Pictures\Screenshots\Screenshot 2026-02-02 233959.png")
sleep(1)

select=driver.find_element(By.NAME,'sgender')
dropdown=Select(select)
dropdown.select_by_value("male")
sleep(1)

driver.find_element(By.XPATH, '//*[@id="container"]/div[8]/input[1]').click()
sleep(1)

driver.find_element(By.XPATH, '//input[@value="automationtesting"]').click()
sleep(1)

select2=driver.find_element(By.ID,'tools')
dropdown2=Select(select2)
dropdown2.select_by_visible_text("Selenium")

driver.find_element(By.ID,'submit').send_keys(Keys.ENTER)

sleep(1)
sleep(5)
driver.quit()