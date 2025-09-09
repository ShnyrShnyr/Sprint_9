import allure
from project.data import Data


class TestCreateRecipe:

    @allure.title('Проверяем, что карточка товара отображается и название рецепта совпадает с ранее вписанным')
    def test_sign_in_and_create_recipe(self, recipes_page, sign_in_page):
        sign_in_page.go_to_sign_in_page()
        sign_in_page.sign_in(Data.EMAIL, Data.PASSWORD)
        expected_name_recipe = Data.NAME_RECIPE
        actual_name_recipe, condition = recipes_page.create_recipe()
        assert actual_name_recipe == expected_name_recipe and condition == True, 'Название рецепта не совпадает с объявленным ранее или Не отображается часть карточки рецепта'
