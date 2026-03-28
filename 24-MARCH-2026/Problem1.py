from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

driver.get("https://codepen.io/gdw96/pen/jOypoYL")

wait.until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))
sleep(3)
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("hiten paliwal")

sleep(3)
driver.find_element(By.ID, "password").send_keys("12345678")

sleep(3)
eye_icon = driver.find_element(By.CLASS_NAME, "fa-eye")

sleep(3)
actions.click_and_hold(eye_icon).perform()
sleep(2)
actions.release().perform()

sleep(3)
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

sleep(1)
sleep(5)
driver.back()
sleep(3)

iframe= driver.find_element(By.ID,'result')
driver.switch_to.frame(iframe)

heading = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="container"]/h1')))

assert "Registration" in heading.text


driver.quit()