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
select.select_by_value("19") # ищем элемент с текстом "Python" #work
time.sleep(2)
x = select.select_by_visible_text("17") #work
print(x.text)
time.sleep(2)
select.select_by_index(4) #work
time.sleep(3)