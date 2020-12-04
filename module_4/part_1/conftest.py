import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="choose language"
    )

@pytest.fixture
def language_choice(request):
    return request.config.getoption("--language")



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
