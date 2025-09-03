import allure
from selenium.webdriver.common.by import By

from project.data import Data
from project.pages.base_page import BasePage

class RegistrationPage(BasePage):
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/signup"]'
    FIRST_NAME_FIELD = By.XPATH, '//input[@name="first_name"]'
    LAST_NAME_FIELD = By.XPATH, '//input[@name="last_name"]'
    USER_NAME_FIELD = By.XPATH, '//input[@name="username"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="email"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="password"]'
    CREATE_ACCOUNT_BUTTON = By.XPATH, '//button[contains(@class,"1FFWl")]'
    REGISTRATION_HEADER = By.XPATH, '//h1[text()="Регистрация"]'
    SIGN_IN_BUTTON = By.XPATH, '//a[@href="/signin"]'


    @allure.step("Нажать на войти на странице регистрации")
    def click_on_sign_in(self):
        self.click_on_element(self.SIGN_IN_BUTTON)

    @allure.step("Перейти на страницу регистрации")
    def go_to_registration_page(self):
        self.go_to_url(Data.MAIN_PAGE_URL + Data.SIGN_IN_PAGE_URL)

    @allure.step("Создать аккаунт")
    def create_account(self, data):
        self.click_on_element(self.REGISTRATION_BUTTON)
        firstname = data.get('firstname','Не сгенерировалось имя')
        self.add_text_to_element(self.FIRST_NAME_FIELD, firstname)
        lastname = data.get('lastname','Не сгенерировалась фамилия')
        self.add_text_to_element(self.LAST_NAME_FIELD, lastname)
        username = data.get('username', 'Не сгенерировалось имя пользователя')
        self.add_text_to_element(self.USER_NAME_FIELD, username)
        email = data.get('email', 'Не сгенерировался email')
        self.add_text_to_element(self.EMAIL_FIELD, email)
        password = data.get('password', 'Не сгенерировался пароль')
        self.add_text_to_element(self.PASSWORD_FIELD, password)
        self.click_on_element(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Проверить, что перестал быть виден заголовок Регистрация")
    def check_redirect_to_sign_in(self):
        self.waiting_to_invisible_element(self.REGISTRATION_HEADER)
        return True



