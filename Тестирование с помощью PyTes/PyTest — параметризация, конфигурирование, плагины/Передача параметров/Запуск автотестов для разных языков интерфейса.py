#Передача языка через Headers; для запуска тестов с определенным языком
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

#firefox
"""
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
"""

"""
эта структура устарела: 

fp = webdriver.FirefoxProfile()

fp.set_preference("intl.accept_languages", user_language)

актуальном считается вот это:

from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference("intl.accept_languages", user_language)
driver_browser = webdriver.Firefox(options=options)
"""