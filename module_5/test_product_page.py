from .pages.main_page import MainPage
from .pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class TestProductPage:
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.check_add_to_cart_notification()
        page.check_total_cart_sum()

