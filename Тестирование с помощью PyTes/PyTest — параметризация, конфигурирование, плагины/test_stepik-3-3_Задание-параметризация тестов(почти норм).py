import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math

@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(15)
    yield browser
    browser.quit()

lessons =   [
            'https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1'
            ]
# lessons = ['https://stepik.org/lesson/236895/step/1']

@pytest.mark.parametrize('lesson', lessons)
def test_stepik_auto_answer(browser, lesson):
    browser.get(lesson)
    
    # Логин
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth_login"))
    ).click()
    
    # Данные для входа
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
    ).send_keys("1max197@mail.ru")

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))
    ).send_keys("123456")
    #browser.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("123456")
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    
    # Ждем загрузки страницы с заданием
    time.sleep(8)
    
    # Вводим ответ в текстовое поле
    answer_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
    )
    answer = str(math.log(int(time.time())))
    #time.sleep(5) #++++
    answer_field.send_keys(answer)
    
    # Отправляем ответ
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    #time.sleep(10)
    
    #Сравнение чек поля
    test_value = browser.find_element(By.CSS_SELECTOR, "div.show-more__content p.smart-hints__hint")
    answer_for_time = test_value.text
    # print(answer_for_time, "+++")
    # time.sleep(10)
    assert answer_for_time == "Correct!"
    answer_for_time = test_value.text

    reset_button = browser.find_element(By.CSS_SELECTOR, "div.attempt__actions button.again-btn.white")
    time.sleep(2)
    reset_button.click()
    time.sleep(5)

