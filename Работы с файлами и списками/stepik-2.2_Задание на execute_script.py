from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
x = browser.find_element(By.CSS_SELECTOR, "#input_value")


answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer_for_x = calc(x.text)
#_ = button.location_once_scrolled_into_view #находит кординаты элемента, например которогоне видно,смещает туда курсор
#print(_)
answer.send_keys(answer_for_x)

browser.execute_script("return arguments[0].scrollIntoView(true);", button) #через js
chekbox_IMtheROBOT = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
chekbox_IMtheROBOT.click()

radiobutton_RobotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radiobutton_RobotsRule.click()

button.click()
time.sleep(3)