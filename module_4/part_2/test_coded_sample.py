import time

link = "http://selenium1py.pythonanywhere.com/ru/"
my_email = "jopa02@mail.ru"
my_pass = "Ujdyjbp;jgs"

def test_user_can_register(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    browser.find_element_by_id('login_link').click()

    browser.find_element_by_css_selector('[name="registration-email"]').clear()
    browser.find_element_by_css_selector('[name="registration-email"]').send_keys(my_email)
    browser.find_element_by_css_selector('[name="registration-password1"]').clear()
    browser.find_element_by_css_selector('[name="registration-password1"]').send_keys(my_pass)
    browser.find_element_by_css_selector('[name="registration-password2"]').clear()
    browser.find_element_by_css_selector('[name="registration-password2"]').send_keys(my_pass)
    browser.find_element_by_css_selector('[name="registration_submit"]').click()
    reg_alert = browser.find_element_by_css_selector('div.alertinner')

    assert reg_alert.text == "Спасибо за регистрацию!", "Reristration failed"
    time.sleep(5)








