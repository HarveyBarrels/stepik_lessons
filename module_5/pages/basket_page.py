from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart_message(self):
        cart_empty_text = "Your basket is empty."
        actual_message = self.browser.find_element(*BasketPageLocators.CART_EMPTY_MESSAGE).text
        assert cart_empty_text in actual_message, "Cart is empty message is not present"

    def should_not_be_any_product_in_cart(self):
        result = self.is_not_element_present(*BasketPageLocators.ITEMS_IN_CART)
        assert result, "Basket is not empty!"


