from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
try:
    name = driver.find_element(By.ID, 'name')
    name.send_keys("hiten")

    email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
    email.send_keys('hitenpaliwal097@gmail.com')

    phone = driver.find_element(By.ID, 'phone')
    phone.send_keys('81079725728')

    address = driver.find_element(By.ID, 'textarea')
    address.send_keys('udaipur')

    radio = driver.find_element(By.ID, 'male')
    radio.click()

    day = driver.find_element(By.XPATH, '//label[text()="Monday"]')
    day.click()
    day.click()

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for i in days:
        click_day = driver.find_element(By.XPATH, '//label[text()="' + i + '"]')
        click_day.click()

    for i in days:
        click_day = driver.find_element(By.XPATH, '//label[text()="' + i + '"]')
        click_day.click()

    sleep(5)

    male=driver.find_element(By.ID, 'male')
    male.click()

    print(male.is_displayed())
    print(male.is_enabled())

    check=driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
    check.click()

    print(check.is_selected())
    mondays=driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
    print(mondays.text)

finally:
    driver.quit()

