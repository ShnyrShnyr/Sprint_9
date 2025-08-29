from selenium.webdriver.common.by import By


class SignInPageLocators:
    CREATE_RECIPES_BUTTON = By.XPATH, '//a[@href="/recipes/create"]'
    SIGN_IN_HEADER = By.XPATH, '//h1[@class="styles_title__2fhty"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="email"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="password"]'
    SIGN_IN_BUTTON = By.XPATH, '//button[contains(@class,"1FFWl")]'
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/signup"]'
    EXIT_BUTTON = By.XPATH, '//a[text()="Выход"]'

