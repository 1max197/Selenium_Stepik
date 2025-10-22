import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
#https://stepik.org/lesson/181384/step/3
import math

"""Скрипт может управлять появлением кнопки на странице и 
показывать ее, например, с задержкой, чтобы кнопка 
красиво и медленно возникала на странице. 
В этом случае наш тест упадет с уже известной нам ошибкой NoSuchElementException, 
так как в момент выполнения команды button = browser.find_element(By.ID, "verify") 
элемент с id="verify" еще не отображается на странице. 
На данной странице пауза перед появлением кнопки установлена на 1 секунду,
 метод find_element() сделает только 
одну попытку найти элемент и в случае неудачи уронит наш тест."""


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
