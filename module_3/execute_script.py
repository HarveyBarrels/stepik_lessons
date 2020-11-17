from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    ans = browser.find_element_by_id('answer')
    ans.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    imrobot = browser.find_element_by_id('robotCheckbox')
    imrobot.click()
    robotsrule = browser.find_element_by_id('robotsRule')
    robotsrule.click()

    button.click()
    time.sleep(5)

finally:
    browser.quit()