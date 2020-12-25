from .base_page import BasePage
from .locators import AccountPageLocators
from selenium.webdriver.support.ui import Select

class AccountPage(BasePage):

    def add_new_user_address(self, first_name, last_name, first_line, city, post_code, country):
        addr_book_tab = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK_TAB)
        addr_book_tab.click()
        add_new_addr_button = self.browser.find_element(*AccountPageLocators.NEW_ADDRESS_BUTTON)
        add_new_addr_button.click()
        self.browser.find_element(*AccountPageLocators.FIRST_NAME_FIELD).send_keys(first_name)
        self.browser.find_element(*AccountPageLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.browser.find_element(*AccountPageLocators.FIRST_LINE_FIELD).send_keys(first_line)
        self.browser.find_element(*AccountPageLocators.CITY_FIELD).send_keys(city)
        self.browser.find_element(*AccountPageLocators.POST_CODE_FIELD).send_keys(post_code)
        country_sel = Select(self.browser.find_element(*AccountPageLocators.COUNTRY_SELECT))
        country_sel.select_by_value(country)
        self.browser.find_element(*AccountPageLocators.SAVE_ADDR_BUTTON).click()

    def check_address_created_msg(self, expected_create_msg):
        actual_msg = self.browser.find_element(*AccountPageLocators.ADDRESS_EDIT_MSG)

        assert expected_create_msg in actual_msg.text, "Address created message is not present"

    def edit_user_address(self, second_line, third_line, state, phone, instructions):
        addr_book_tab = self.browser.find_element(*AccountPageLocators.ADDRESS_BOOK_TAB)
        addr_book_tab.click()
        edit_addr_button = self.browser.find_element(*AccountPageLocators.EDIT_ADDR_BUTTON)
        edit_addr_button.click()
        self.browser.find_element(*AccountPageLocators.SECOND_LINE_FIELD).send_keys(second_line)
        self.browser.find_element(*AccountPageLocators.THIRD_LINE_FIELD).send_keys(third_line)
        self.browser.find_element(*AccountPageLocators.STATE_FIELD).send_keys(state)
        self.browser.find_element(*AccountPageLocators.PHONE_NUMBER_FIELD).send_keys(phone)
        self.browser.find_element(*AccountPageLocators.INSTR_FIELD).send_keys(instructions)
        self.browser.find_element(*AccountPageLocators.SAVE_ADDR_BUTTON).click()

    def check_address_edited_msg(self, expected_edit_msg):
        actual_msg = self.browser.find_element(*AccountPageLocators.ADDRESS_EDIT_MSG)

        assert expected_edit_msg in actual_msg.text, "Address edited message is not present"

    def shoul_not_be_address_exist_msg(self):
        result = self.is_not_element_present(*AccountPageLocators.ADDRESS_ERROR_MSG)
        assert result, "Address editing error is present!"

    def delete_user_profile(self, confirm_pass):
        del_profile_btn = self.browser.find_element(*AccountPageLocators.DELETE_PROFILE_BTN)
        del_profile_btn.click()
        pass_input =  self.browser.find_element(*AccountPageLocators.CONFIFM_PASS_TO_DEL_PROFILE)
        pass_input.send_keys(confirm_pass)
        confirm_del_btn = self.browser.find_element(*AccountPageLocators.CONFIRM_DEL_PROFILE_BTN)
        confirm_del_btn.click()










