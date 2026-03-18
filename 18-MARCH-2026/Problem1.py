from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/")


checkboxes_link = driver.find_element(By.LINK_TEXT, "Checkboxes")

drag_and_drop_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")


li_elements = driver.find_elements(By.TAG_NAME, "li")
print("Total li element:", len(li_elements))


driver.get("https://the-internet.herokuapp.com/tables")


website = driver.find_element(
    By.XPATH,
    "//table[@id='table1']//td[text()='jdoe@hotmail.com']/ancestor::tr/td[5]"
)


delete_link = driver.find_element(
    By.XPATH,
    "//table[@id='table1']//td[text()='Bach']/ancestor::tr//a[text()='delete']"
)


second_table = driver.find_element(By.XPATH, "(//table)[2]")


cell = driver.find_element(
    By.XPATH,
    "//table[@id='table2']//td[text()='$100.00']"
)

parent_row = cell.find_element(By.XPATH, "./ancestor::tr")


sleep(3)
driver.quit()