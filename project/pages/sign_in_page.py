import allure
from selenium.webdriver.common.by import By

from project.data import Data
from project.pages.base_page import BasePage
from project.pages.registration_page import RegistrationPage


@allure.description("Страница авторизации")
class SignInPage(BasePage):
    CREATE_RECIPES_BUTTON = By.XPATH, '//a[@href="/recipes/create"]'
    SIGN_IN_HEADER = By.XPATH, '//h1[@class="styles_title__2fhty"]'
    EMAIL_FIELD = By.XPATH, '//input[@name="email"]'
    PASSWORD_FIELD = By.XPATH, '//input[@name="password"]'
    SIGN_IN_BUTTON = By.XPATH, '//button[contains(@class,"1FFWl")]'
    REGISTRATION_BUTTON = By.XPATH, '//a[@href="/signup"]'
    EXIT_BUTTON = By.XPATH, '//a[text()="Выход"]'
    SIGN_IN_FORM_EMAIL = By.XPATH, '//div[text()="Электронная почта"]'
    SIGN_IN_FORM_PASSWORD = By.XPATH, '//div[text()="Пароль"]'


    @allure.step("Перейти на страницу авторизации")
    def go_to_sign_in_page(self):
        self.go_to_url(Data.MAIN_PAGE_URL + Data.SIGN_IN_PAGE_URL)

    @allure.step("Авторизация")
    def sign_in(self, email, password):
        self.add_text_to_element(self.EMAIL_FIELD, email)
        self.add_text_to_element(self.PASSWORD_FIELD, password)
        self.click_on_element(self.SIGN_IN_BUTTON)


    @allure.step("Проверить, что видны элементы электронная почта и пароль")
    def check_visible_sign_in_form(self):
        self.check_element_visible(self.SIGN_IN_FORM_EMAIL)
        self.check_element_visible(self.SIGN_IN_FORM_PASSWORD)
        return True
