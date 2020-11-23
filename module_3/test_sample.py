from selenium import webdriver
import time

main_page_link = "http://selenium1py.pythonanywhere.com/ru/"

def test_add_to_cart():
    item_to_buy = "Coders at Work"
    item_to_buy_locator = '[title = "Coders at Work"]'
    try:
        #Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)
        browser.find_element_by_css_selector('[href = "/ru/catalogue/"]').click()
        #Act
        browser.find_element_by_css_selector(item_to_buy_locator).click()
        browser.find_element_by_css_selector('[value = "Добавить в корзину"]').click()
        #basket_add_notify = browser.find_element_by_css_selector('#messages>:nth-child(1)>div')  #элемент-оповещение об успешном добавлении
        browser.find_element_by_link_text("Посмотреть корзину").click()
        #Assert
        added_item_link = browser.find_element_by_css_selector('#content_inner h3>a')
        #assert basket_add_notify.text == f"{item_to_buy} был добавлен в вашу корзину.", "Item not added to basket"
        assert added_item_link.text == item_to_buy, f"{item_to_buy} was not added to cart"
    finally:
        time.sleep(5)
        browser.quit()

test_add_to_cart()
