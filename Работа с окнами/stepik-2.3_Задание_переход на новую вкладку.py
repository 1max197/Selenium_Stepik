import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
#https://stepik.org/lesson/184253/step/6
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

Flying_button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
Flying_button.click()

new_window = browser.window_handles[1]
first_window = new_window
browser.switch_to.window(first_window)

Submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
x = calc(x)
Input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
Input_field.send_keys(x)
Submit.click()
time.sleep(4)