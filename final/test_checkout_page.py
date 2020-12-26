from .pages.checkout_page import CheckoutPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.lang_pack import lang_dict

#Data
link = "http://selenium1py.pythonanywhere.com/"
email = 'sometestmail@mail.ru'
password = 'sometestpass'

class TestCheckoutPage:
    def test_user_can_make_order(self, browser):
        #Arrange
        page_lang = browser.user_language
        order_confirm_msg_template = lang_dict[page_lang]['order_confirm_msg_template']
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_to_account(email, password)
        page.should_be_authorized_user()
        page.go_to_catalogue()
        page.add_first_product_to_cart_from_catalogue()
        page.go_to_basket_page()
        cart_page = BasketPage(browser, browser.current_url)
        #Act
        cart_page.proceed_to_checkout()
        checkout_page = CheckoutPage(browser, browser.current_url)
        checkout_page.do_simple_checkout()
        #Assert
        checkout_page.should_be_order_confirm_msg(order_confirm_msg_template)
