import allure
from page_object.data import Data
from page_object.locators.registration_page_locators import RegistrationPageLocators
from page_object.locators.sign_in_page_locators import SignInPageLocators
from page_object.pages.base_page import BasePage


@allure.description("Страница авторизации")
class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на войти")
    def click_on_create_account(self):
        self.click_on_element(SignInPageLocators.REGISTRATION_BUTTON)
        return self.find_element_with_wait(RegistrationPageLocators.REGISTRATION_HEADER)

    @allure.step("Авторизация")
    def sign_in(self):
        self.add_text_to_element(SignInPageLocators.EMAIL_FIELD,Data.EMAIL)
        self.add_text_to_element(SignInPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.click_on_element(SignInPageLocators.SIGN_IN_BUTTON)
        element = self.find_element_with_wait(SignInPageLocators.EXIT_BUTTON)
        return element

    def check_redirect_to_recipes(self):
        current_url = self.get_url()
        return current_url

