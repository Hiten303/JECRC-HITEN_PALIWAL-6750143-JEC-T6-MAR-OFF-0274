
from time import sleep


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)

# driver.get("https://www.abc.com")
# driver.implicitly_wait(5)
# ele=driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute('src'))

# wait = WebDriverWait(driver, 10,poll_frequency=200)
# submit_button = wait.until(EC.element_to_be_clickable((By.ID,'button')))
# submit_button.click()


driver.get('https://demoqa.com/dynamic-properties')

multi_select=driver.find_element(By.ID,'//select[@id="multi-select-s"]')
select=Select(multi_select)
if select.is_multiple():
    select.select_by_value('8')
    select.select_by_index(6)
    select.select_by_visible_text('Movies, Music & Games')

sleep(3)
select.deselect_by_index(6)
select.deselect_all()
print(select.first_selected_option)
print(select.all_selected_options)
driver.quit()
