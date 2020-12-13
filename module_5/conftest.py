import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language: ru, en-GB, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    my_language = request.config.getoption("language")
    my_options = Options()
    my_options.add_argument(f"--lang={my_language}")

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=my_options)
    browser.user_language = my_language


    yield browser
    print("\nquit browser..")
    browser.quit()