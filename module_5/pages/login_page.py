from .base_page import BasePage
from .main_page import MainPage
from .locators import  LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        page = MainPage(self.browser, self.url)
        page.go_to_login_page()
        curr_url = self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert "login" in curr_url, "Login url is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
