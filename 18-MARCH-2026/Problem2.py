from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")




driver.find_element(By.ID, "firstName").send_keys("Hiten")
sleep(1)

driver.find_element(By.ID, "lastName").send_keys("Paliwal")
sleep(1)

driver.find_element(By.ID, "userEmail").send_keys("hitenpaliwal097@gmail.com")
sleep(1)

driver.find_element(By.XPATH, "//label[text()='Male']").click()
sleep(1)

driver.find_element(By.ID, "userNumber").send_keys("1234567890")

sleep(1)


subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)
sleep(1)
subjects.send_keys("Physics")
subjects.send_keys(Keys.ENTER)
sleep(1)

driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Music']").click()
sleep(1)

driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\user\OneDrive\Documents\Pictures\Screenshots\Screenshot 2026-02-02 233959.png")
sleep(1)

driver.find_element(By.ID, "currentAddress").send_keys("Jaipur, Rajasthan")
sleep(1)


state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("Rajasthan")
state.send_keys(Keys.ENTER)
sleep(1)

city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Jaipur")
city.send_keys(Keys.ENTER)
sleep(1)

driver.find_element(By.ID, "submit").click()
sleep(1)
sleep(5)
driver.quit()