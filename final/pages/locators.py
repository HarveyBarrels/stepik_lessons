from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#id_q")
    SEARCH_BTN = (By.CSS_SELECTOR, "div.primary.navbar-inverse input.btn")
    #search_page
    FOUND_PRODUCT_LINK = (By.CSS_SELECTOR, "article.product_pod>h3>a")

class BasketPageLocators:
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div.content #content_inner")
    ITEMS_IN_CART = (By.CSS_SELECTOR, "div.content div.basket-items")
    GO_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, "#content_inner a.btn-block")

class MainPageLocators():
    CATALOGUE_LINK = (By.CSS_SELECTOR, "li.active.open>ul.dropdown-menu>:nth-child(1)>a")
    ADD_PRD_FROM_CAT_BTN = (By.CSS_SELECTOR, "section article button")
    DEL_PROFILE_SUCCESS_MSG = (By.CSS_SELECTOR, "div.alertinner.wicon")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#register_form [name= 'registration-email']")
    REG_PASS = (By.CSS_SELECTOR, "#register_form [name= 'registration-password1']")
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, "#register_form [name= 'registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "#register_form [name= 'registration_submit']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#login_form [name = 'login-username']")
    LOGIN_PASS = (By.CSS_SELECTOR, "#login_form [name = 'login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login_form [name = 'login_submit']")

class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ADD_TO_CART_NOTIFICATION = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
    #PRODUCT_NAME_HEADER = (By.CSS_SELECTOR, ".product_main h1")
    CART_SUM_NOTIFICATION = (By.CSS_SELECTOR, "div.alert-info .alertinner")
    DISPLAYED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")

class AccountPageLocators:
    ADDRESS_BOOK_TAB = (By.CSS_SELECTOR, ".nav-pills li:nth-child(3) > a")
    NEW_ADDRESS_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "[name = 'first_name']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "[name = 'last_name']")
    FIRST_LINE_FIELD = (By.CSS_SELECTOR, "[name = 'line1']")
    SECOND_LINE_FIELD = (By.CSS_SELECTOR, "[name = 'line2']")
    THIRD_LINE_FIELD = (By.CSS_SELECTOR, "[name = 'line3']")
    CITY_FIELD = (By.CSS_SELECTOR, "[name = 'line4']")
    STATE_FIELD = (By.CSS_SELECTOR, "[name = 'state']")
    POST_CODE_FIELD = (By.CSS_SELECTOR, "[name = 'postcode']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "[name = 'country']")
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, "[name = 'phone_number']")
    INSTR_FIELD = (By.CSS_SELECTOR, "[name = 'notes']")
    SAVE_ADDR_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg")
    ADDRESS_EDIT_MSG = (By.CSS_SELECTOR, "div.alertinner.wicon")
    EDIT_ADDR_BUTTON = (By.CSS_SELECTOR, "div.btn-group a.btn.btn-default")
    ADDRESS_ERROR_MSG = (By.CSS_SELECTOR, "div.alert-danger")
    DELETE_PROFILE_BTN = (By.CSS_SELECTOR, "#delete_profile")
    CONFIFM_PASS_TO_DEL_PROFILE = (By.CSS_SELECTOR, "[name = 'password']")
    CONFIRM_DEL_PROFILE_BTN = (By.CSS_SELECTOR, "button.btn-danger")

class CheckoutPageLocators:
    SHIP_TO_THIS_ADDR_BTN = (By.CSS_SELECTOR, "button.ship-address")
    PAYMENT_CONFIRM_BTN = (By.CSS_SELECTOR, "#view_preview")
    PLACE_ORDER_BTN = (By.CSS_SELECTOR, "#place-order")
    ORDER_CONFIRM_MSG = (By.CSS_SELECTOR, "p.lead")
