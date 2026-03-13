from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com")
driver.maximize_window()

time.sleep(3)

# 1 ID locator
logo = driver.find_element(By.ID, "cb-logo-main-menu")
print("Logo found")

# 2 Link Text locator
matches = driver.find_element(By.LINK_TEXT, "Matches")
print("Menu:", matches.text)

# 3 Class Name locator
news = driver.find_elements(By.CLASS_NAME, "cb-nws-hdln")

print("Top News:")
for n in news[:5]:
    print(n.text)

# 4 XPath locator
first_match = driver.find_element(By.XPATH, "(//div[@class='cb-mtch-lst cb-col cb-col-100 cb-tms-itm'])[1]")
print("First Match Block Found")

# 5 CSS Selector locator
videos = driver.find_elements(By.CSS_SELECTOR, "h4.cb-vid-title")

print("Videos:")
for v in videos[:3]:
    print(v.text)

time.sleep(5)
driver.quit()