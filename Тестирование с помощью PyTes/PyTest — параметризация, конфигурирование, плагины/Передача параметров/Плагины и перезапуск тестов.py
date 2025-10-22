#https://docs.pytest.org/en/latest/explanation/flaky.html#plugins
#https://docs.pytest.org/en/latest/reference/plugin_list.html
#pip install pytest-rerunfailures #плагин для перезапуска упавших тестов
#pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py #"--tb=line", чтобы сократить лог с результатами теста; "--reruns n", где n — это количество перезапусков.
#pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

#pytest -v --tb=line --reruns 1 --browser_name=chrome "Тестирование с помощью PyTes\PyTest — параметризация, конфигурирование, плагины\PyTest — параметризация, конфигурирование, плагины\Передача параметров\Плагины и перезапуск тестов.py"
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_pas_2(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")


#1 failed, 2 passed, 1 rerun in 25.97s