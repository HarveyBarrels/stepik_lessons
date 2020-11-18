from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    subbut = browser.find_element_by_css_selector("[type = 'submit']")
    subbut.click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0] #чтобы вернуться к первому окну
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    subbut2 = browser.find_element_by_css_selector("[type = 'submit']")
    subbut2.click()
    time.sleep(10)

finally:
    browser.quit()