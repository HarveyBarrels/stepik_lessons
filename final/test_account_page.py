from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage
from final.pages.account_page import AccountPage
import pytest
import time

#Data
link = "http://selenium1py.pythonanywhere.com/"
email = 'sometestmail@mail.ru'
password = 'sometestpass'
first_name = 'Somename'
last_name = 'Somelastname'
first_line = 'Someline'
city = 'Somecity'
post_code = '428000'
country = 'RU'
second_line = 'some 2nd line'
third_line =  'some 3rd line'
state = 'some state'
phone = '+74955556677'
instructions = 'do something there'
expected_create_msg = 'created'
expected_update_msg = 'updated'

del_profile_msg_template = 'Your profile has now been deleted'


class TestAccountPage:

    def test_user_can_add_new_address(self, browser):
        #Arrange
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_to_account(email, password)
        login_page.go_to_account_page()
        #Act
        acnt_page = AccountPage(browser, browser.current_url)
        acnt_page.add_new_user_address(first_name, last_name, first_line, city, post_code, country)
        #Assert
        acnt_page.shoul_not_be_address_exist_msg()
        acnt_page.check_address_created_msg(expected_create_msg)


    def test_user_can_edit_address(self, browser):
        #Arrange
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login_to_account(email, password)
        login_page.go_to_account_page()
        #Act
        acnt_page = AccountPage(browser, browser.current_url)
        acnt_page.edit_user_address(second_line, third_line, state, phone, instructions)
        #Assert
        acnt_page.shoul_not_be_address_exist_msg()
        acnt_page.check_address_edited_msg(expected_update_msg)

    @pytest.mark.del_profile
    def test_user_can_delete_account(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        tmp_email = str(time.time()) + "@fakemail.org"
        tmp_password = "testpassword"
        login_page.register_new_user(tmp_email, tmp_password)
        login_page.go_to_account_page()
        #Act
        acnt_page = AccountPage(browser, browser.current_url)
        acnt_page.delete_user_profile(tmp_password)
        #Assert
        page.should_be_deleted_profile_message(del_profile_msg_template)







