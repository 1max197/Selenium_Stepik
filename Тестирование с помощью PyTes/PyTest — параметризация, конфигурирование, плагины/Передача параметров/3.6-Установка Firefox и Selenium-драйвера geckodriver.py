#pytest -s -v --browser_name=firefox test_cmd.py #запуск другого браузера
from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

#https://github.com/mozilla/geckodriver/releases #geckodriver
#Для Windows не забудьте добавить в системную переменную PATH папку C:\geckodriver и перезапустить командную строку, чтобы путь стал доступен.