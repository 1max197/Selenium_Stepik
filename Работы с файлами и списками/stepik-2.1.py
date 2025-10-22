#import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

""""
driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://suninjuly.github.io/text_input_task.html")
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

textarea.send_keys("get()")
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

submit_button.click()
time.sleep(5)


driver.quit()

"""

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")
#ime.sleep(5)

x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
input_for_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
input_for_answer.send_keys(y)

chekbox_IMtheROBOT = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
chekbox_IMtheROBOT.click()

radiobutton_RobotsRule = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
radiobutton_RobotsRule.click()
                                              #tn btn-default
Submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
Submit_button.click()                                        
time.sleep(5)
print(y)