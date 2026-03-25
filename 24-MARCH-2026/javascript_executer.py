from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
# driver.execute_script('console.log("helo");')
sleep(3)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)
driver.execute_script('window.scrollTo(0,0);')
sleep(2)

# using scroll by
driver.execute_script('window.scrollBy(0,500);')
sleep(2)
driver.execute_script('window.scrollBy(0,-200);')
sleep(2)

# ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
ele=driver.find_element(By.XPATH,'(//button[@data-test-id="join-pinterest-button-homepage-redesign-signup-flow"])[3]')

sleep(3)
driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(3)
driver.execute_script('arguments[0].click();',ele)
sleep(3)
driver.quit()
