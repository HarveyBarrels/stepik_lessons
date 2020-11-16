from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    sunduk  = browser.find_element_by_id("treasure")
    x = sunduk.get_attribute("valuex")
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    imrobot = browser.find_element_by_id('robotCheckbox')
    imrobot.click()
    robotsrule = browser.find_element_by_id('robotsRule')
    robotsrule.click()
    subbut = browser.find_element_by_css_selector("[type='submit']")
    subbut.click()

finally:
    time.sleep(10)
    browser.quit()