from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_TO_CART_NOTIFICATION = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    #PRODUCT_NAME_HEADER = (By.CSS_SELECTOR, ".product_main h1")
    CART_SUM_NOTIFICATION = (By.CSS_SELECTOR, "div.alert-info .alertinner")
    DISPLAYED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
