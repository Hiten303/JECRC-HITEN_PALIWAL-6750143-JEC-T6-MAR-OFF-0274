from time import sleep
from selenium import webdriver

browser = ["chrome", "edge"]

for i in browser:

    if i == "chrome":
        driver = webdriver.Chrome()
        driver.get("https://google.com")

    elif i == "edge":
        driver = webdriver.Edge()
        driver.get("https://google.com")

    print(driver.current_url)
    print(driver.title)

    sleep(1)
    driver.close()