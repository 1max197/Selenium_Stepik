from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        #self.current_url = self.browser.current_url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            #self.browser.find_element(how, what)
            self.element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    
    def click_on_element(self, WebElement = None):
        try:
            print(f" Click on {self.element.text} ")
            self.element.click()
        except NoSuchElementException:
            return False
        return True
    
    def get_text_for_element(self):
        try:
            #print(f" Getting '{self.element.text}' - text for element {self.element.accessible_name} text from BasePage")
            self.element.text
        except NoSuchElementException:
            return False
        return self.element.text
        #WebElement.click()

    #ждет пока вернут тру и вернет фалсе / упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый. 
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    #ждет пока вернут фалсе и вернет тру / будет ждать до тех пор, пока элемент не исчезнет. 
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True