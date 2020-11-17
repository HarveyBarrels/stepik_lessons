from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    name = browser.find_element_by_css_selector("[name = 'firstname']")
    name.send_keys('Ivan')
    surname = browser.find_element_by_css_selector("[name = 'lastname']")
    surname.send_keys('Govnov')
    mail = browser.find_element_by_css_selector("[name = 'email']")
    mail.send_keys('govnov@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    loadfile = browser.find_element_by_id('file')
    loadfile.send_keys(file_path)
    subbut = browser.find_element_by_css_selector('[type = "submit"]')
    subbut.click()
    time.sleep(5)

finally:
    browser.quit()