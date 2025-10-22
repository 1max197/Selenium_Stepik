#import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/get_attribute.html")

hiden_value = browser.find_element(By.CSS_SELECTOR, '#treasure')
hiden_value_attr = hiden_value.get_attribute("valuex")
x = calc(hiden_value_attr)

radio_robots_rule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radio_robots_rule.click()

chexbox_ImtheRobot = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
chexbox_ImtheRobot.click()

input_for_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
input_for_answer.send_keys(x)

Submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
Submit_button.click()  

time.sleep(3)
print(x)