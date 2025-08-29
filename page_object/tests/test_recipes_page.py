import allure

from page_object.data import Data
from page_object.tests.conftest import recipes_page


class TestRecipesPage:
    @allure.title('Проверяем, что карточка товара отображается и название рецепта совпадает с ранее вписанным')
    def test_sign_in_and_create_recipe(self, recipes_page, sign_in_page):
        _ = sign_in_page.sign_in()
        element, actual_name_recipe = recipes_page.create_recipe()
        expected_name_recipe = Data.NAME_RECIPE
        assert element.is_displayed() and expected_name_recipe == actual_name_recipe