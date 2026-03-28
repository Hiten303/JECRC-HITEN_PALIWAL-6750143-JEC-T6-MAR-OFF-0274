from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver,10)
action = ActionChains(driver)

driver.get('https://www.cleartrip.com/')


wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@data-testid="loginPopup"]/div/div[2])[1]'))).click()

assert 'https://www.cleartrip.com/' == driver.current_url, 'URL is wrong'



fromCity= wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Where from?"]')))
fromCity.send_keys('Udaipur')
sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH,'(//li[@class="m-1"])[1]'))).click()



toCity = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Where to?"]')))
toCity.send_keys('Bengaluru')
sleep(1)
wait.until(EC.element_to_be_clickable((By.XPATH,'(//li[@class="m-1"])[1]'))).click()




departure = wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@data-testid="dateSelectOnward"]')))
departure.click()

month_year = 'Jan 2027'
date = '1'

while True:

    month = wait.until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="DayPicker-Month"]/div[1]/div)[1]')))
    if month.text == month_year:
        break
    else:
        sleep(1)
        right_arrow = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div[class="flex-1 ta-right"] svg')))
        action.move_to_element(right_arrow).perform()
        action.click(right_arrow).perform()


datepicker = wait.until(EC.visibility_of_element_located((By.XPATH,f'(//div[text()={date}])[1]')))
datepicker.click()
sleep(2)

flight = wait.until(EC.element_to_be_clickable((By.XPATH,'//h4[text()="Search flights"]/ancestor::button')))
flight.click()

fl = driver.find_element(By.XPATH,'//div[@class="sc-aXZVg dczbns mb-2 bg-white"]')
print(fl.text)






sleep(2)
driver.quit()