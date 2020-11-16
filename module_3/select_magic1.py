from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    elem_a = browser.find_element_by_id("num1")
    elem_b = browser.find_element_by_id("num2")
    a = elem_a.text
    b = elem_b.text
    sum = str(int(a) + int(b))
    sel = Select(browser.find_element_by_tag_name("select"))
    sel.select_by_value(sum)
    subbut = browser.find_element_by_css_selector("[type='submit']")
    subbut.click()

finally:
    time.sleep(10)
    browser.quit()