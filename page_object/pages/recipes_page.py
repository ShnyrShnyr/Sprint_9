from pathlib import Path

from page_object.data import Data
from page_object.locators.recipes_page_locators import RecipesPageLocators
from page_object.locators.sign_in_page_locators import SignInPageLocators
from page_object.pages.base_page import BasePage


class RecipesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_recipe(self):
        self.click_on_element(SignInPageLocators.CREATE_RECIPES_BUTTON)
        self.add_text_to_element(RecipesPageLocators.NAME_OF_RECIPES_FIELD, Data.NAME_RECIPE)
        for i in range(1, 4):
            # Формируем имена атрибутов
            i = str(i)
            ingr_name = f'INGREDIENT_{i}'
            dropdown_name = f'INGREDIENT_{i}_DROPDOWN'
            qty_name = f'INGREDIENT_{i}_QUANTITY'

            # Достаём из классов нужные локаторы и данные

            dropdown_locator  = getattr(RecipesPageLocators, dropdown_name)
            ingr_text         = getattr(Data, ingr_name)
            qty_text          = getattr(Data, qty_name)

            # Выполняем действия
            self.add_text_to_element(RecipesPageLocators.INGREDIENT, ingr_text)
            self.click_on_element(dropdown_locator)
            self.add_text_to_element(RecipesPageLocators.INGREDIENT_QUANTITY, qty_text)
            self.click_on_element(RecipesPageLocators.ADD_INGREDIENT)

        self.add_text_to_element(RecipesPageLocators.COOKING_TIME_FIELD, Data.COOKING_TIME)
        self.add_text_to_element(RecipesPageLocators.DESCRIPTION_FIELD, Data.DESCRIPTION)
        APP_DIR = Path(__file__).parent
        file_path = APP_DIR / 'assets' / 'Omlet.jpg'
        self.find_element_with_wait(RecipesPageLocators.LOAD_FILE_BUTTON).send_keys(file_path)
        self.click_on_element(RecipesPageLocators.CREATE_RECIPE_BUTTON)
        element = self.find_element_with_wait(RecipesPageLocators.CARD_OF_RECIPE)
        actual_name_recipe = self.get_text_from_element(RecipesPageLocators.NAME_OF_RECIPES_HEADER)
        return element, actual_name_recipe
