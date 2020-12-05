def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)

    page_language = browser.find_element_by_css_selector("[selected='selected']").get_attribute('value')
    cart_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    expect_button_text = None
    if page_language == 'ru':
        expect_button_text = "Добавить в корзину"
    elif page_language == 'en-gb':
        expect_button_text = "Add to basket"
    elif page_language == 'es':
        expect_button_text = "Añadir al carrito"
    elif page_language == 'fr':
        expect_button_text = "Ajouter au panier"
    else:
        print("\nSelected language is not tested")

    assert cart_button.text == f"{expect_button_text}", f"Button text wrong, expected '{expect_button_text}', got '{cart_button.text}'"
