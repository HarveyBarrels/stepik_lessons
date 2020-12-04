def test_guest_should_see_add_to_cart_button(browser, language_choice):
    link = f"http://selenium1py.pythonanywhere.com/{language_choice}/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    if language_choice == "ru":
       expect_button_text = "Добавить в корзину"
    elif language_choice == "en-gb":
       expect_button_text = "Add to basket"


    assert button.text == f"{expect_button_text}", f"Button text wrong, expected {expect_button_text}, got {button.text}"
