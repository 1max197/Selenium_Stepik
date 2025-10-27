from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
#import time
# cd "/c/Projects Python/Тестирование с помощью PyTes/Page Object"
# pytest --browser_name=chrome --language=ru tests/test_main_page.py 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    #time.sleep(5)

def test_guest_not_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.not_should_be_login_link()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#реализация перехода между страницами
def test_guest_can_go_to_login_page_trough(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def  test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page_by_init_page_b_class()
    login_page.should_be_login_page()

#pytest -s -v -m "testbuttonbasket" tests/test_main_page.py
@pytest.mark.testbuttonbasket
def test_guest_cant_see_product_in_basket_opened_from_main_page_trough_clickselftest(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    page = MainPage(browser, link)
    page.open()
    page.click_on_button_seebasket_trough_selftest()
    basket_page = BasketPage(page.browser, page.browser.current_url)
    basket_page.not_should_be_basket_items()
    basket_page.should_be_text_basket_is_empty()
    #BasketPage.not_should_be_basket_items(page) #work