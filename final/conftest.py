import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: ru, en-GB, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    my_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        my_options = Options()
        my_options.add_argument(f"--lang={my_language}")
        print("\nstart browser chrome for test..")
        browser = webdriver.Chrome(options=my_options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", my_language)
        print("\nstart browser firefox for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))

    browser.user_language = my_language

    yield browser
    print("\nquit browser..")
    browser.quit()