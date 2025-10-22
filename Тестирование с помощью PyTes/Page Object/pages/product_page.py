from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from pages.locators import ProductPageLocators
import time

#from selenium import webdriver


class ProductPage(BasePage):

    def should_be_basket_button(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*ProductPageLocators.BASKET), "Basket button is absence"
    
    def should_be_basket_button_clickable(self):
        assert self.click_on_element(), "Basket button is not clickable"

    def should_be_form_goods_after_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.TEXTGOODS_AFTER_BUSKET_ADDING), "Formgoods is absence"

    def should_be_name_For_good(self):
        assert self.is_element_present(*ProductPageLocators.NAME_FOR_GOODS), "Name for good is absence"
        #self.name_for_good = self.get_text_for_element()

    def get_text_for_good_name(self):
        self.should_be_name_For_good()
        good_name = self.get_text_for_element()
       # print(good_name, "'is a good name'")
        return good_name
    
    def get_text_for_good_name_in_added_to_cart_message_displays(self):
        self.should_be_form_goods_after_add_to_basket()
        good_name = self.get_text_for_element()
       # print(good_name, "'is a good name after basket'")
        return good_name

    def added_to_cart_message_displays_correct_product_name(self):
        print(self.get_text_for_good_name() , "+++" , self.get_text_for_good_name_in_added_to_cart_message_displays())
        assert self.get_text_for_good_name() in self.get_text_for_good_name_in_added_to_cart_message_displays() , "Text good is not equal to text after adding to basket"

    def added_to_cart_message_displays_correct_clause(self):
        print(self.get_text_for_good_name() , "+++" , self.get_text_for_good_name_in_added_to_cart_message_displays())
        print(self.get_text_for_good_name() + " был добавлен в вашу корзину" , "+++" , self.get_text_for_good_name_in_added_to_cart_message_displays())
        assert self.get_text_for_good_name() + " был добавлен в вашу корзину." == self.get_text_for_good_name_in_added_to_cart_message_displays() , "Text clause is not equal to text after adding to basket"
 ############################################################
    def should_be_form_goodsprice_after_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.TEXTPRICEGOODS_AFTER_BUSKET_ADDING), "Formprice is absence"
    #
    def should_be_goodsprice(self):
        assert self.is_element_present(*ProductPageLocators.PRICEGOODS), "Formprice is absence"

    def get_goodprice(self):
        self.should_be_goodsprice()
        goodprice = self.get_text_for_element()
       # print(good_name, "'is a good name'")
        return goodprice
    
    def get_goodprice_in_added_to_cart_message_displays(self):
        self.should_be_form_goodsprice_after_add_to_basket()
        goodprice_at_cart_message= self.get_text_for_element()
       # print(good_name, "'is a good name'")
        return goodprice_at_cart_message
    
    def added_to_cart_goodprice_displays_correct_product_price(self):
        print(self.get_goodprice() , "+++" , self.get_goodprice_in_added_to_cart_message_displays())
        assert self.get_goodprice() in self.get_goodprice_in_added_to_cart_message_displays() , "Goodprice is not equal to Goodprice after adding to basket"

################################################################
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #time.sleep(10)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

##################################################################
    def should_not_be_success_message(self):
        print("Я сделал этот шаг")
        assert self.is_not_element_present(*ProductPageLocators.TEXTGOODS_AFTER_BUSKET_ADDING), \
        "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.TEXTGOODS_AFTER_BUSKET_ADDING), \
        "Success message is presented, but should not be"