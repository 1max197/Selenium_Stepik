import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
#https://stepik.org/lesson/181384/step/6

"""
Если элемент не был найден за отведенное время, 
то мы получим NoSuchElementException.
Если элемент был найден в момент поиска,
 но при последующем обращении к элементу 
 DOM изменился, то получим StaleElementReferenceException. 
 Например, мы нашли элемент Кнопка и через какое-то время решили 
 выполнить с ним уже известный нам метод click. 
 Если кнопка за это время была скрыта скриптом, 
 то метод применять уже бесполезно — элемент 
 "устарел" (stale) и мы увидим исключение.
Если 
элемент был найден в момент поиска, 
но сам элемент невидим (например, имеет нулевые размеры), 
и реальный пользователь не смог бы с ним взаимодействовать, 
то получим ElementNotVisibleException.
"""
browser = webdriver.Chrome()
browser.implicitly_wait(5) 

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
#button.click()
