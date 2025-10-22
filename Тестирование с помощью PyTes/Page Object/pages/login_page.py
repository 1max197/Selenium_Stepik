from pages.base_page import BasePage
from pages.locators import LoginPageLocators
#from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in LoginPageLocators.LOGIN_URL, "Login substring is absence"
    
    def should_be_login_url_from_property_of_webdriwer(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login substring is absence"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is absence"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is absence"

    def not_should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FALSE_LOGIN_FORM), "Login form is absence"

    def not_should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FALSE_REGISTER_FORM), "Register form is absence"