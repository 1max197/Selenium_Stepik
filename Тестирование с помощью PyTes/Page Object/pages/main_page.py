from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url) 
    
    def go_to_login_page_by_init_page_b_class(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url) 


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    
    def not_should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.FALSE_LOGIN_LINK), "Login link is not presented"