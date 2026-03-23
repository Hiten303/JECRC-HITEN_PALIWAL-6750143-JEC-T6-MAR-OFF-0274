

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)


driver.get(r'D:\pycharm\project\20-MARCH-2026\playlist.html')

# songs_list= driver.find_element(By.ID,'songs')
# select = Select(songs_list)

artist=driver.find_elements(By.XPATH,"//optgroup[@label='Ed Sheeran']/option")
# print(artist.text)
for song in artist:
    song.click()
    print(song.text)


sleep(3)
#
# if select.is_multiple:
#
#     for option in select.options:
#
#         text=option.text.lower()
#         # print(option.text)
#         if "love" in text or "girl" in text:
#             select.select_by_visible_text(option.text)
#     # select.select_by_index(4)
#     # select.select_by_visible_text('Shape of You')
#     # select.select_by_visible_text('Animals')

# print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH,'//button[text()="Add to Playlist"]').click()
sleep(3)
# print([i.text for  i in select.options])

sleep(4)
driver.quit()