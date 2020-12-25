from .base_page import BasePage
from .locators import CheckoutPageLocators

class CheckoutPage(BasePage):

    def do_simple_checkout(self):
        self.browser.find_element(*CheckoutPageLocators.SHIP_TO_THIS_ADDR_BTN).click()
        self.browser.find_element(*CheckoutPageLocators.PAYMENT_CONFIRM_BTN).click()
        self.browser.find_element(*CheckoutPageLocators.PLACE_ORDER_BTN).click()

    def should_be_order_confirm_msg(self, order_confirm_msg_template):
        confirm_msg = self.browser.find_element(*CheckoutPageLocators.ORDER_CONFIRM_MSG)
        assert order_confirm_msg_template in confirm_msg.text, "Order was not placed"