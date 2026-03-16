from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
# driver.refresh()
sleep(2)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
search = driver.find_element(By.NAME, "q")
search.send_keys("mobile")
print(search.get_attribute("value"))
search.send_keys(Keys.ENTER)
sleep(2)

images=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div/div/img')
print(images.get_attribute("src"))


brand=driver.find_element(By.CLASS_NAME,"buvtMR")
print(brand.text)
# driver.find_element(By.CLASS_NAME,"ybaCDx").click()
brand.click()
sleep(4)


driver.quit()