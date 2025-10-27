from pages.base_page import BasePage #++++
from pages.locators import LoginPageLocators
import time
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
    
    def register_new_user(self, email, password):
        # EMAIL = str(time.time()) + "@fakemail.org"
        # PASSWORD = "1234"
        #self.browser.find_element(*LoginPageLocators.REGISTER_FORM).click()
        self.browser.find_element(*LoginPageLocators.EMAIL_ON_REGISTER_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_ON_REGISER_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASS_ON_REGISER_FORM_ADMIT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_ADMIT_REG).click()