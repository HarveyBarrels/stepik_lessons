from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_btn.click()

    def check_add_to_cart_notification(self, expected_notification_text):
        actual_notification_text = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_NOTIFICATION).text
        #expected_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_HEADER).text
        assert actual_notification_text == expected_notification_text, f"Product was not added to cart, got:{actual_notification_text}"


    def check_total_cart_sum(self):
        actual_cart_sum_notif = self.browser.find_element(*ProductPageLocators.CART_SUM_NOTIFICATION).text
        expected_product_price = self.browser.find_element(*ProductPageLocators.DISPLAYED_PRODUCT_PRICE).text
        assert expected_product_price in actual_cart_sum_notif, "Total cart sum is wrong"

