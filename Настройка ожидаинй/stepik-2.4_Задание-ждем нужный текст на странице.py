from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #явные ожидания
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
#https://stepik.org/lesson/181384/step/8
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

Book_button = browser.find_element(By.CSS_SELECTOR, "#book") 
Book_button.click()



#time.sleep(3)
# new_window = browser.window_handles[1]
# first_window = new_window
# browser.switch_to.window(first_window)

#Submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
x = calc(x)
Input_field = browser.find_element(By.CSS_SELECTOR, "#answer")
Input_field.send_keys(x)
# WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
#     )
Submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
Submit_button.click()
time.sleep(10)

#EC.element_located_selection_state_to_be
#EC.presence_of_element_located