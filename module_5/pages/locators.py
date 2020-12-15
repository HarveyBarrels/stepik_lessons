from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div.content #content_inner")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "div.content div.basket-items")

#class MainPageLocators():


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#register_form [name= 'registration-email']")
    REG_PASS = (By.CSS_SELECTOR, "#register_form [name= 'registration-password1']")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#register_form [name= 'registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form [name= 'registration_submit']")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_TO_CART_NOTIFICATION = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    #PRODUCT_NAME_HEADER = (By.CSS_SELECTOR, ".product_main h1")
    CART_SUM_NOTIFICATION = (By.CSS_SELECTOR, "div.alert-info .alertinner")
    DISPLAYED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
