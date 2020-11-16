from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    imrobot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    imrobot.click()
    robotsrule = browser.find_element_by_css_selector("[for='robotsRule']")
    robotsrule.click()
    subbut = browser.find_element_by_css_selector("[type='submit']")
    subbut.click()

finally:
    time.sleep(10)
    browser.quit()
