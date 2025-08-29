from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/signup"]'
    FIRST_NAME_FIELD = By.XPATH, '//input[@name="first_name"]'
    LAST_NAME_FIELD = By.XPATH, '//input[@name="last_name"]'
    USER_NAME_FIELD = By.XPATH, '//input[@name="username"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="email"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="password"]'
    CREATE_ACCOUNT_BUTTON = By.XPATH, '//button[contains(@class,"1FFWl")]'
    REGISTRATION_HEADER = By.XPATH, '//h1[text()="Регистрация"]'
    SIGN_IN_BUTTON = By.XPATH, '//a[@href="/signin"]'

