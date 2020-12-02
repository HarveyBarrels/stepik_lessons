import pytest
from selenium import webdriver
import time
import math



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_solve_fuckin_problem(browser, page):
    link = f"https://stepik.org/lesson/{page}/step/1/"
    browser.get(link)
    answer = math.log(int(time.time()))
    anstext = str(answer)
    browser.find_element_by_css_selector("textarea").send_keys(anstext)
    browser.find_element_by_css_selector("button.submit-submission").click()
    feedback = browser.find_element_by_css_selector("pre.smart-hints__hint")

    assert feedback.text == "Correct!", f"Expexted 'Correct!', got '{feedback.text}'"

