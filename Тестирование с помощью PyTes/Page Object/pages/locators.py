from selenium.webdriver.common.by import By
import time

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FALSE_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_false")

class BasePageLocators(MainPageLocators):
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    ELEMENT_TEXT_BASKET_IS_EMTPY = (By.CSS_SELECTOR, "div#content_inner p")
    TEXT_BASKET_IS_EMTPY = "Your basket is empty."
    

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FALSE_LOGIN_FORM = (By.CSS_SELECTOR, "#login_formaaa")
    FALSE_REGISTER_FORM = (By.CSS_SELECTOR, "#register_formaaa")
    EMAIL_ON_REGISTER_FORM = (By.CSS_SELECTOR, "div.form-group div input#id_registration-email")
    PASS_ON_REGISER_FORM = (By.CSS_SELECTOR, "div.form-group div input#id_registration-password1")
    PASS_ON_REGISER_FORM_ADMIT = (By.CSS_SELECTOR, "div.form-group div input#id_registration-password2")
    BUTTON_ADMIT_REG = (By.CSS_SELECTOR, "button[name='registration_submit'][value='Register']")
    # EMAIL = str(time.time()) + "@fakemail.org"
    # PASSWORD = str(time.time()) + "@fakemail.org"



class ProductPageLocators():
    URL = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    URL_2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    URL_3 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    PROMO = "?promo=offer"
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    TEXTGOODS_AFTER_BUSKET_ADDING = (By.CSS_SELECTOR, "div.alert-success div.alertinner" )
    TEXTPRICEGOODS_AFTER_BUSKET_ADDING = (By.CSS_SELECTOR, "div.alert-info div.alertinner > p" )
    PRICEGOODS = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color" )
    NAME_FOR_GOODS = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1" )

# arr = [ProductPageLocators.URL_3 + ProductPageLocators.PROMO + str(i) for i in range(10)]
# print(arr)
    
    
