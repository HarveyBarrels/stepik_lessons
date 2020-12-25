from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
#    def __init__(self, *args, **kwargs):
#        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_catalogue(self):
        catalogue_link = self.browser.find_element(*MainPageLocators.CATALOGUE_LINK)
        catalogue_link.click()

    def add_first_product_to_cart_from_catalogue(self):
        add_to_cart_btn = self.browser.find_element(*MainPageLocators.ADD_PRD_FROM_CAT_BTN)
        add_to_cart_btn.click()

    def should_be_deleted_profile_message(self, del_profile_msg_template):
        del_profile_msg = self.browser.find_element(*MainPageLocators.DEL_PROFILE_SUCCESS_MSG)
        assert del_profile_msg_template in del_profile_msg.text, "Profile was not deleted"
