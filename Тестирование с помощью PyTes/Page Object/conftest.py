import pytest
from selenium import webdriver

#browser_name = request.config.getoption("browser_name")

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: en, ru, fr,")
    parser.addoption("--headless", action="store_true", default=False, help="Run in headless mode")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    language = request.config.getoption("--language")
    headless_mode = request.config.getoption("--headless")
    browser = None
    if browser_name == "chrome" and language in ['en', 'ru', 'fr']:
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless_mode:
            options.add_argument("--headless") #запуск без ui
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox" and language in ['en', 'ru', 'fr']:
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox and lang en ru fr")
    yield browser
    print("\nquit browser..")
    browser.quit()

