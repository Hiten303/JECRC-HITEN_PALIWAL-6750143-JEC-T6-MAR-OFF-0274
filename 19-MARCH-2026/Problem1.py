from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.abc.com")

wait = WebDriverWait(driver, 10)


images=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='hero-items']//div[contains(@class,'tile--hero')]//img[@data-mptype='image']")))


for i in images:
    print(i.get_attribute('src'))

driver.quit()