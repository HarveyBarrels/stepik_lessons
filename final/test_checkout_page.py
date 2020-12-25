from .pages.checkout_page import CheckoutPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

#Data
link = "http://selenium1py.pythonanywhere.com/"
email = 'sometestmail@mail.ru'
password = 'sometestpass'
order_confirm_msg_template = 'Your order has been placed'

class TestCheckoutPage:
    def test_user_can_make_order(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_to_account(email, password)
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
