import os
from pathlib import Path

from selenium.webdriver.common.by import By
from project.data import Data
from project.pages.base_page import BasePage



class RecipesPage(BasePage):
    NAME_OF_RECIPES_FIELD = By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input'
    INGREDIENT = By.XPATH, '//div[text()="Ингредиенты"]/following-sibling::input'
    INGREDIENT_QUANTITY = By.XPATH, '//input[contains(@class,"2matT")]'
    ADD_INGREDIENT = By.XPATH, '//div[@class="styles_ingredientAdd__3fc32"]'
    COOKING_TIME_FIELD = By.XPATH, '//div[text()="Время приготовления"]/following-sibling::input'
    DESCRIPTION_FIELD = By.XPATH, '//textarea'
    LOAD_FILE_BUTTON = By.XPATH, '//input[@type="file"]'
    CREATE_RECIPE_BUTTON = By.XPATH, '//a[text()="Создать рецепт"]'
    NAME_OF_RECIPES_HEADER = By.XPATH, '//h1[contains(@class,"2QMPq")]'
    LIST_OF_ORDERS = By.XPATH, '//a[text()="Список покупок"]'
    FAVORITES = By.XPATH, '//a[text()="Избранное"]'
    CHANGE_FILE_BUTTON = By.XPATH, "//div[@type='button']"
    COOKING_TIME_OF_RECIPE = By.XPATH, '//p[contains(@class,"2_OKG")]'
    INGREDIENTS_OF_RECIPE = By.XPATH, '//h3[text()="Ингридиенты:"]'
    DESCRIPTION_OF_RECIPE = By.XPATH, '//h3[text()="Описание:"]'
    CREATE_RECIPE_BUTTON_DOWN = By.XPATH, '//button[contains(@class,"f_Q9Z")]'

    def create_recipe(self):
        self.click_on_element(self.CREATE_RECIPE_BUTTON)
        self.add_text_to_element(self.NAME_OF_RECIPES_FIELD, Data.NAME_RECIPE)
        for i, j, k in zip(
            Data.INGREDIENT_DATA,
            Data.INGREDIENT_DROPDOWN,
            Data.INGREDIENT_QUANTITY_DATA
        ):
            self.add_text_to_element(self.INGREDIENT, i)
            dropdown_locator = By.XPATH, j
            self.click_on_element(dropdown_locator)
            self.add_text_to_element(self.INGREDIENT_QUANTITY, k)
            self.click_on_element(self.ADD_INGREDIENT)

        self.add_text_to_element(self.COOKING_TIME_FIELD, Data.COOKING_TIME)
        self.add_text_to_element(self.DESCRIPTION_FIELD, Data.DESCRIPTION)

        APP_DIR = Path(__file__).resolve().parent.parent
        file_path = APP_DIR / 'assets' / 'cafe_milk.jpg'
        input_file = self.find_element_with_wait_in_dom(self.LOAD_FILE_BUTTON)
        input_file.send_keys(str(file_path.resolve()))
        self.click_on_element(self.CREATE_RECIPE_BUTTON_DOWN)
        condition = True
        while condition == True:
            condition = self.check_element_visible(self.COOKING_TIME_OF_RECIPE)
            if condition == False:
                print('Не отображается время приготовления')
                break
            condition = self.check_element_visible(self.INGREDIENTS_OF_RECIPE)
            if condition == False:
                print('Не отображаются ингредиенты рецепта')
                break
            condition = self.check_element_visible(self.DESCRIPTION_OF_RECIPE)
            break
        actual_name_recipe = self.get_text_from_element(self.NAME_OF_RECIPES_HEADER)
        return actual_name_recipe, condition

    def check_redirect_to_recipes_page(self):
        self.check_element_visible(self.LIST_OF_ORDERS)
        self.check_element_visible(self.FAVORITES)
        self.check_element_visible(self.CREATE_RECIPE_BUTTON)
        return True


