#from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from pages.locators import LoginPageLocators
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest
# cd "/c/Projects Python/Тестирование с помощью PyTes/Page Object"
# pytest --browser_name=chrome --language=ru tests/test_product_page.py 
# pytest -v -s -rx --browser_name=chrome --language=ru tests/test_product_page.py::test_there_is_success_message_to_basket tests/test_product_page.py::test_there_is_not_success_message_to_basket
# pytest -s -v -m "testbuttonbasket" tests/test_product_page.py
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

@pytest.mark.testbuttonbasket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_seebasket()

@pytest.mark.testbuttonbasket
def test_guest_cant_see_product_in_basket_opened_from_product_page_trough_clickselftest(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_button_seebasket_trough_selftest()
    basket_page = BasketPage(page.browser, page.browser.current_url)
    basket_page.not_should_be_basket_items()
    basket_page.should_be_text_basket_is_empty()
    #BasketPage.not_should_be_basket_items(page) #work

    ##################CLASSS###########################################

#Класс шаблон, ничего не делает
@pytest.mark.skip
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

@pytest.mark.testroughclass
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        EMAIL = str(time.time()) + "@fakemail.org"
        PASSWORD = str(time.time()) + "@fakemail.org"
        link = LoginPageLocators.LOGIN_URL
        self.loginpage = LoginPage(browser, link)
        self.loginpage.open()
        self.loginpage.register_new_user(email=EMAIL, password=PASSWORD)
        self.loginpage.should_be_authorized_user()
        yield

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.URL_2
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.URL_2
        page = ProductPage(browser, link)
        page.open()
        page.click_on_basket_button() #new
        page.solve_quiz_and_get_code()
        page.should_be_form_goods_after_add_to_basket()
        page.get_text_for_good_name()
        page.added_to_cart_message_displays_correct_product_name()
        page.added_to_cart_message_displays_correct_clause()
        page.should_be_form_goodsprice_after_add_to_basket()
        page.should_be_goodsprice()
        page.added_to_cart_goodprice_displays_correct_product_price()