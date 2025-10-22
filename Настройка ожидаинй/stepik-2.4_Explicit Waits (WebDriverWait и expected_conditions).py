from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #явные ожидания
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#https://stepik.org/lesson/181384/step/7

"""
browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
"""

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
"""
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
"""
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text