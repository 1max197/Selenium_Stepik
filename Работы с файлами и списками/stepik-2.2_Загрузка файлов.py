from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
#https://stepik.org/lesson/184253/step/2

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
# как принять алеерт
alert = browser.switch_to.alert
alert.accept()
alert_text = alert.text #получить текст из алерт
"""
Другой вариант модального окна, который предлагает пользователю 
выбор согласиться с сообщением или отказаться от него, называется confirm
"""
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()# отказ
"""
Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. 
Чтобы ввести текст, используйте метод send_keys():
"""
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()


