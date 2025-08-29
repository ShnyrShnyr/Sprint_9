import allure
import pytest

from page_object.locators.registration_page_locators import RegistrationPageLocators
from page_object.locators.sign_in_page_locators import SignInPageLocators
from page_object.pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на войти")
    def click_on_sign_in(self):
        self.click_on_element(RegistrationPageLocators.SIGN_IN_BUTTON)
        return self.find_element_with_wait(SignInPageLocators.SIGN_IN_HEADER)


    def create_account(self, data):
        self.click_on_element(RegistrationPageLocators.REGISTRATION_BUTTON)
        firstname = data.get('firstname','Не сгенерировалось имя')
        self.add_text_to_element(RegistrationPageLocators.FIRST_NAME_FIELD, firstname)
        lastname = data.get('lastname','Не сгенерировалась фамилия')
        self.add_text_to_element(RegistrationPageLocators.LAST_NAME_FIELD, lastname)
        username = data.get('username', 'Не сгенерировалось имя пользователя')
        self.add_text_to_element(RegistrationPageLocators.USER_NAME_FIELD, username)
        email = data.get('email', 'Не сгенерировался email')
        self.add_text_to_element(RegistrationPageLocators.EMAIL_FIELD, email)
        password = data.get('password', 'Не сгенерировался пароль')
        self.add_text_to_element(RegistrationPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON)
        element = self.find_element_with_wait(SignInPageLocators.SIGN_IN_HEADER)
        return element

    def check_redirect_to_sign_in(self):
        self.waiting_to_invisible_element(RegistrationPageLocators.REGISTRATION_HEADER)
        current_url = self.get_url()
        return current_url

    def check_visible_sign_in_form(self, locator):
        return self.check_element_visible(locator)

