from selenium import webdriver
import time
import unittest

class regtest(unittest.TestCase):

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector('.first_block .first')
        first_name.send_keys('Ivan')
        second_name = browser.find_element_by_css_selector('.first_block .second')
        second_name.send_keys('Pipiskin')
        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys('IP@mail.ru')
        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Registration error")
        browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        first_name = browser.find_element_by_css_selector('.first_block .first')
        first_name.send_keys('Ivan')
        second_name = browser.find_element_by_css_selector('.first_block .second')
        second_name.send_keys('Pipiskin')
        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys('IP@mail.ru')
        time.sleep(2)
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', "Registration error")
        browser.quit()

if __name__ == "__main__":
    unittest.main()