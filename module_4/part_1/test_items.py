
lang_dict = {
    'ru' : {'add_to_cart_button_text' : 'Добавить в корзину',
            'some_other_shit' : 'жопа'},
    'en-gb' : {'add_to_cart_button_text' : 'Add to basket',
                'some_other_shit' :'asshole'},
    'es' : {'add_to_cart_button_text' : 'Añadir al carrito',
            'some_other_shit' : 'spanish ass'},
    'fr' : {'add_to_cart_button_text' : 'Ajouter au panier',
            'some_other_shit' : 'french ass'}
}

def test_guest_should_see_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)

    page_language = browser.user_language
    cart_button = browser.find_element_by_css_selector("button.btn-add-to-basket")

    expect_button_text = lang_dict[page_language]['add_to_cart_button_text']

    print(expect_button_text)

    assert cart_button.text == f"{expect_button_text}", f"Button text wrong, expected '{expect_button_text}', got '{cart_button.text}'"
