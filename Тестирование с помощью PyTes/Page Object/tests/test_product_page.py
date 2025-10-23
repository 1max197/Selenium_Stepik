#from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import time
import pytest
# cd "/c/Projects Python/Тестирование с помощью PyTes/Page Object"
# pytest --browser_name=chrome --language=ru tests/test_product_page.py 
##pytest -v -s -rx --browser_name=chrome --language=ru tests/test_product_page.py::test_there_is_success_message_to_basket tests/test_product_page.py::test_there_is_not_success_message_to_basket

def test_guest_can_add_product_to_basket_by_ckick_by_basepage(browser):
    link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_basket_button()
    page.click_on_element() # #дергаем метод из BaseObject 
    #time.sleep(5)
    #page.click_on_element(WebElement=page.should_be_basket_button)
    page.solve_quiz_and_get_code()  
    page.should_be_form_goods_after_add_to_basket()
    page.get_text_for_good_name()
    page.added_to_cart_message_displays_correct_product_name()

    page.should_be_form_goodsprice_after_add_to_basket()
    page.should_be_goodsprice()
    page.added_to_cart_goodprice_displays_correct_product_price()


    #time.sleep(100000000)
    

def test_guest_can_add_product_to_basket_by_shouldbe_basket_button_clickable(browser):
    link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_basket_button()
    page.should_be_basket_button_clickable() #дергаем метод из PageObject обьекта
    #time.sleep(5)
    page.solve_quiz_and_get_code()

    page.should_be_form_goods_after_add_to_basket()
    page.get_text_for_good_name()
    page.added_to_cart_message_displays_correct_product_name()
    page.should_be_form_goodsprice_after_add_to_basket()
    page.should_be_goodsprice()
    page.added_to_cart_goodprice_displays_correct_product_price()

    #time.sleep(10)

"""
x = "123"
y = "321"
arr = [x+y+str(i) for i in range(10)]
arr = [f"{x}+{y}+{str(i)}" for i in range(10)]
"""
# ('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",]
# )
#[ProductPageLocators.URL_3 + ProductPageLocators.PROMO + str(i) for i in range(10)]
#pytest -s -rx --reruns 1 --browser_name=chrome --language=ru tests/test_product_page.py::test_guest_can_add_product_to_basket
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail(reason="invald clause in basket")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # ваша реализация теста
    #link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_basket_button_clickable() #дергаем метод из PageObject обьекта
    #time.sleep(5)
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_be_form_goods_after_add_to_basket()
    page.get_text_for_good_name()
    page.added_to_cart_message_displays_correct_product_name()
    page.added_to_cart_message_displays_correct_clause()
    page.should_be_form_goodsprice_after_add_to_basket()
    page.should_be_goodsprice()
    page.added_to_cart_goodprice_displays_correct_product_price()

@pytest.mark.negativetask
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_basket_button_clickable() #дергаем метод из PageObject обьекта
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()

@pytest.mark.negativetask
def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
  
    page.should_not_be_success_message()

@pytest.mark.negativetask
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.URL_2
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.should_be_basket_button_clickable() #дергаем метод из PageObject обьекта
    page.solve_quiz_and_get_code()
  
    page.should_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_go_product_page_by_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = page.go_to_login_page_by_init_page_b_class()
