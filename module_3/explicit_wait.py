from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    btn = browser.find_element_by_id('book')
    btn.click()
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    subbut = browser.find_element_by_css_selector('[type = "submit"]')
    subbut.click()
    time.sleep(10)

finally:
    browser.quit()