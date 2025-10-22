#import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/selects1.html")

#Работа со списками по старинке
"""
browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
browser.find_element(By.CSS_SELECTOR, "[value='1']").click()
"""
# 
#Работа через класс Select

#select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown.custom-select")) #тоже ок 
select = Select(browser.find_element(By.TAG_NAME, "select")) #тоже ок

x = browser.find_element(By.CSS_SELECTOR, "#num1").text #пишет число
x = int(x)
print(x, type(x))

y = browser.find_element(By.CSS_SELECTOR, "#num2").text
y = int(y)
print(y, type(y))

xy = x + y
select.select_by_value(str(xy))

Submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
Submit_button.click() 
time.sleep(3)