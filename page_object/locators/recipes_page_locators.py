from selenium.webdriver.common.by import By


class RecipesPageLocators:

    NAME_OF_RECIPES_FIELD = By.XPATH, '//div[text()="Название рецепта"]/following-sibling::input'
    INGREDIENT = By.XPATH, '//div[text()="Ингредиенты"]/following-sibling::input'
    INGREDIENT_1_DROPDOWN = By.XPATH, '//div[text()="молоко 2,5%"]'
    INGREDIENT_2_DROPDOWN = By.XPATH, '//div[text()="яйца куриные крупные"]'
    INGREDIENT_3_DROPDOWN = By.XPATH, '//div[text()="соль морская"]'

    INGREDIENT_QUANTITY = By.XPATH, '//input[contains(@class,"2matT")]'
    ADD_INGREDIENT = By.XPATH, '//div[@class="styles_ingredientAdd__3fc32"]'
    COOKING_TIME_FIELD = By.XPATH, '//div[text()="Время приготовления"]/following-sibling::input'
    DESCRIPTION_FIELD = By.XPATH, '//textarea'
    LOAD_FILE_BUTTON = By.XPATH, '//input[@type="file"]'
    CREATE_RECIPE_BUTTON = By.XPATH, '//button[text()="Создать рецепт"]'
    NAME_OF_RECIPES_HEADER = By.XPATH, '//h1[contains(@class,"2QMPq")]'
    CARD_OF_RECIPE = By.XPATH, '//div[contains(@class,"2_cny")]'
