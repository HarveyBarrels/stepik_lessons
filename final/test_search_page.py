from final.pages.main_page import MainPage
import  pytest

link = "http://selenium1py.pythonanywhere.com/"

class TestSearchPage:
    @pytest.mark.parametrize('template', ["The shellcoder's handbook", "Coders at Work", "popka"])
    def test_search_is_working(self, browser, template):
        #Arrange
        search_template = f"{template}"
        page = MainPage(browser, link)
        page.open()
        #Act
        page.product_search(search_template)
        #Assert
        page.should_find_product(search_template)


