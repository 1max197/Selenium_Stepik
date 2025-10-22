import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
#https://stepik.org/lesson/184253/step/4
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

I_want = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
I_want.click()

new_window = browser.window_handles[1]
first_window = new_window
browser.switch_to.window(first_window)
time.sleep(3)