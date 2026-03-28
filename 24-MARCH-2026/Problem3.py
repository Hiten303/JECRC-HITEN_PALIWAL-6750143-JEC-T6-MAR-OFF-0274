from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/browser-windows")

main_window = driver.current_window_handle

driver.find_element(By.ID, "tabButton").click()
sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])

text = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading"))).text
assert "This is a sample page" in text

driver.close()
driver.switch_to.window(main_window)

print("New Tab Passed")


driver.find_element(By.ID, "windowButton").click()
sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[1])

text = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading"))).text
assert "This is a sample page" in text

driver.close()
driver.switch_to.window(main_window)

print("New Window Passed")


driver.find_element(By.ID, "messageWindowButton").click()
sleep(2)

windows = driver.window_handles

driver.switch_to.window(windows[1])

texts = driver.find_element(By.XPATH, '//body[contains(),"knowledge increases by sharing"]')
print(texts.text)

assert "Knowledge increases by sharing but not by saving" in text

driver.close()
driver.switch_to.window(main_window)

print("Message Window Passed")

driver.quit()