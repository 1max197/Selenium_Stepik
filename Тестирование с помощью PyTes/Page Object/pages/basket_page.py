from pages.base_page import BasePage
from pages.locators import BasketPageLocators
# from pages.locators import MainPageLocators
# from pages.login_page import LoginPage
# from selenium.webdriver.common.by import By

class BasketPage(BasePage): 

    def not_should_be_basket_items(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "BASKTE ITEMS link is not present" # .basket-items

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.ELEMENT_TEXT_BASKET_IS_EMTPY), "text_basket is not present" # .basket-items
        #assert self.get_text_for_element() == BasketPageLocators.TEXT_BASKET_IS_EMTPY, f"incorrect text, should be {BasketPageLocators.TEXT_BASKET_IS_EMTPY}, but give {self.get_text_for_element()}"
        assert self.get_text_for_element().strip().startswith(BasketPageLocators.TEXT_BASKET_IS_EMTPY), f"incorrect text, should be {BasketPageLocators.TEXT_BASKET_IS_EMTPY}, but give {self.get_text_for_element()}"


