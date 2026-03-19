from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://www.amazon.in/")
search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("laptop")
searches=wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@class="left-pane-results-container"]/div[4]')))
searches.click()
wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-action="a-dropdown-button"]'))).click()
wait.until(EC.presence_of_element_located((By.ID,'s-result-sort-select_4'))).click()

wait.until(EC.presence_of_element_located((By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[1]'))).click()
sleep(2)

product = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="a-section a-spacing-small a-spacing-top-small"]//h2')))
sleep(2)
print(product.get_attribute('aria-label'))
sleep(2)


price = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="a-price"]/child::span')))
print(price.get_attribute('innerHTML'))

sleep(5)
driver.quit()






