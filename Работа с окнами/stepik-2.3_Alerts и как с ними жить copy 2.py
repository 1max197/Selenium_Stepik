import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#https://stepik.org/lesson/184253/step/2

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

#всплывающая хуйня на сайтах
alert = browser.switch_to.alert
alert.accept()
alert_text = alert.text

confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

#такая же + ввести текст
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
