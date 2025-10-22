#http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ #где тестить
#pytest --language=es test_items.py #так запускать
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_there_is_a_bin (browser):
    browser.get(link)
    time.sleep(5)
    biin = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    assert biin == "Добавить в корзину" or "Add to basket"

def test_there_is_no_bin(browser):
    browser.get(link)
    time.sleep(5)
    biin = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket").text
    rewiew = browser.find_element(By.CSS_SELECTOR, "#write_review").text
    assert rewiew == biin 

# cd "/c/Projects Python/Тестирование с помощью PyTes/PyTest — параметризация, конфигурирование, плагины/Передача параметров"
#pytest --reruns 1 --browser_name=chrome --language=en ./Задание_запуск\ автотестов\ для\ разных\ языков\ интерфейса.py
#pytest --reruns 1 --browser_name=chrome --language=en --headless ./Задание_запуск\ автотестов\ для\ разных\ языков\ интерфейса.py
"""
# С языком
pytest --browser_name=chrome --language=ru

# В headless режиме
pytest --browser_name=firefox --headless

# Со всеми опциями
pytest --browser_name=chrome --language=fr --headless
"""