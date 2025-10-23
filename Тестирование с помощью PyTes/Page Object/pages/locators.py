from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FALSE_LOGIN_LINK = (By.CSS_SELECTOR, "#login_link_false")

class BasePageLocators(MainPageLocators):
    pass

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
   
    FALSE_LOGIN_FORM = (By.CSS_SELECTOR, "#login_formaaa")
    FALSE_REGISTER_FORM = (By.CSS_SELECTOR, "#register_formaaa")

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
    
    
