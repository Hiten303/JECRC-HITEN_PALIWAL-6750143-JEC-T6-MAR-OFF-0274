from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
sleep(3)


wait = WebDriverWait(driver, 10)

assert "Amazon" in driver.title, "Failed"
sleep(2)
assert "amazon.in" in driver.current_url, "Failed"
sleep(2)

search = driver.find_element(By.ID,'twotabsearchtextbox')
search.send_keys('Headphones')
search.send_keys(Keys.ENTER)
sleep(3)

brand = driver.find_element(By.XPATH,'(//i[@class="a-icon a-icon-checkbox"])[5]')
brand.click()
sleep(3)

driver.find_element(By.XPATH,'//li[@id="p_36/dynamic-picker-0"]/child::span/a').click()
sleep(3)

driver.find_element(By.XPATH,'(//span[@class="rush-component"])[4]').click()
sleep(3)

product = driver.find_element(By.XPATH,'//a[@class="a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/child::h2/span')
print(product.text)

productPrice = driver.find_element(By.XPATH,'(//span[@class="a-price-whole"])[1]')
print(productPrice.text)

products= driver.window_handles
driver.switch_to.window(products[1])

productTiteAfter= driver.find_element(By.XPATH,'//span[@id="productTitle"]')
print(productTiteAfter.text)

productPriceAfter= driver.find_element(By.XPATH,'(//span[@class="a-price-whole"])[1]')
print(productPriceAfter.text)

driver.find_element(By.ID,'add-to-cart-button').click()
driver.find_element(By.XPATH,'//a[contains(text(),"Go to Cart")]').click()

cart= driver.find_element(By.XPATH,'//span[@class="a-truncate-cut"]')
print(cart.text)

cartPrice = driver.find_element(By.XPATH,'//span[@class="a-price a-text-price sc-product-price sc-white-space-nowrap a-size-medium"]')
print(cartPrice.text)



driver.quit()