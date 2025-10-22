from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
#_ = button.location_once_scrolled_into_view #находит кординаты элемента, например которогоне видно,смещает туда курсор
#print(_)
time.sleep(3)
browser.execute_script("return arguments[0].scrollIntoView(true);", button) #через js
button.click()
time.sleep(3)