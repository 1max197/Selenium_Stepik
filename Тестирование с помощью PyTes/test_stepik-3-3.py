import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #явные ожидания
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=chrome_options)
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.implicitly_wait(15)

    yield browser
    print("\nquit browser..")
    browser.quit()

# lessons =   [
#             'https://stepik.org/lesson/236895/step/1',
#             'https://stepik.org/lesson/236896/step/1',
#             'https://stepik.org/lesson/236897/step/1',
#             'https://stepik.org/lesson/236898/step/1',
#             'https://stepik.org/lesson/236899/step/1',
#             'https://stepik.org/lesson/236903/step/1',
#             'https://stepik.org/lesson/236904/step/1',
#             'https://stepik.org/lesson/236905/step/1'
#             ]
lessons =   [
            'https://stepik.org/lesson/236895/step/1'
            ]

@pytest.mark.parametrize('lesson', lessons)
def test_guest_should_see_login_link(browser, lesson):
    link = lesson
    browser.get(link)

    login_button = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    login_button.send_keys("1max1977@mail.ru")

    pass_button = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    pass_button.send_keys("7$k9n2UXyWw8sD5B") #sign-form__btn button_with-loader 

    input_button = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    input_button.click()

#     """
#     #через гугл
#     input_button = browser.find_element(By.CSS_SELECTOR, "#ember484")
#     input_button.click()
#     """
#     ##################
#     """
#     #через гугл
#     google_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-block.btn-social.btn-google")
#     google_button.click()
#     google_mail_button = browser.find_element(By.CSS_SELECTOR, "#identifierId")
#     google_mail_button.send_keys("    ")
#     """
#     #next_button = browser.find_element(By.XPATH, "//*[@id='identifierNext']/div/button")#work
#     next_button = browser.find_element(By.CSS_SELECTOR, "#identifierNext")
#     next_button.click()
#     ##################
#     """
#     #через гугл
#     pass_button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
#     pass_button.send_keys("  ")
#     """
#     next_button = browser.find_element(By.CSS_SELECTOR, "#passwordNext")
#     next_button.click()
#     time.sleep(5)
#     ##################
#     #ember550
#     answer_field = WebDriverWait(browser, 12).until(EC.visibility_of(browser.find_element(By.CSS_SELECTOR, "div.quiz-component.ember-view textarea")))
#     #answer_field = browser.find_element(By.CSS_SELECTOR, "div.attempt textarea")
#     answer = math.log(int(time.time()))
#     answer_field.send_keys(answer)
#     #time.sleep(10)
#     ##################
#     answer_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
#     answer_button.click()
#    # time.sleep(10)
#     ##################
#     test_value = browser.find_element(By.CSS_SELECTOR, "div.show-more__content p.smart-hints__hint")
#     answer_for_time = test_value.text
#     print(answer_for_time, "+++")
#     time.sleep(10)
#    # assert answer_for_time == "Correct"

  

#answer_field = WebDriverWait(browser, 12).until(EC.visibility_of((By.CSS_SELECTOR, "div.quiz-component.ember-view textarea]")))
 # print(f"Element displayed: {pass_button.is_displayed()}")
    # print(f"Element enabled: {pass_button.is_enabled()}")
    # print(f"Element location: {pass_button.location}")
    # print(f"Element size: {pass_button.size}")
    # browser.save_screenshot("debug.png")
    ##################