from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
import time


lang_dict = {
    "ru: qwert"
    "en-gb: riuh"
    "es: kjhefkjh"
    "fr: jkshejfh"
    }

#product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestProductPage:
    @pytest.mark.skip(reason="Not needed at this step")
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        product_param_link = f"{link}"
        expected_product_name = "Coders at Work"
        expected_notification_template = "{} has been added to your basket."
        page = ProductPage(browser, product_param_link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        expected_notification_text = expected_notification_template.format(expected_product_name)
        page.check_add_to_cart_notification(expected_notification_text)
        page.check_total_cart_sum()

    @pytest.mark.skip(reason="Not needed at this step")
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        #отрицательная проверка - отсутствие сообщения об успешном добавлении в корзину (на странице корзины)
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart()
        result = page.is_not_element_present(*ProductPageLocators.ADD_TO_CART_NOTIFICATION)
        assert result, "Success message is present"

    @pytest.mark.skip(reason="Not needed at this step")
    def test_guest_cant_see_success_message(self, browser):
        # отрицательная проверка - отсутствие сообщения об успешном добавлении в корзину (на странице товара)
        page = ProductPage(browser, product_link)
        page.open()
        result =  page.is_not_element_present(*ProductPageLocators.ADD_TO_CART_NOTIFICATION)
        assert result, "Success message is present"

    @pytest.mark.skip(reason="Not needed at this step")
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # отрицательная проверка (исчезание сообщения о добавлении в корзину)
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart()
        result = page.is_disappeared(*ProductPageLocators.ADD_TO_CART_NOTIFICATION)
        assert result, "Message has not dissapeared"

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_basket_page()
        cart_page = BasketPage(browser, browser.current_url)
        cart_page.should_be_empty_cart_message()
        cart_page.should_not_be_any_product_in_cart()

@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage: #тесты для зарегистрированного пользователя

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # отрицательная проверка - отсутствие сообщения об успешном добавлении в корзину (на странице товара)
        page = ProductPage(browser, product_link)
        page.open()
        result =  page.is_not_element_present(*ProductPageLocators.ADD_TO_CART_NOTIFICATION)
        assert result, "Success message is present"

    def test_user_can_add_product_to_basket(self, browser):
        expected_product_name = "Coders at Work"
        expected_notification_template = "{} has been added to your basket."
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart()
        expected_notification_text = expected_notification_template.format(expected_product_name)
        page.check_add_to_cart_notification(expected_notification_text)
        page.check_total_cart_sum()
