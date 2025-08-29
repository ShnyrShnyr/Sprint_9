import allure
import pytest

from page_object.data import Data
from page_object.locators.sign_in_page_locators import SignInPageLocators
from page_object.tests.conftest import sign_in_page


class TestRegistrationPage:

    @allure.title('Проверка регистрации')
    def test_click_on_create_account(self, sign_in_page):
        element = sign_in_page.click_on_create_account()
        assert element.is_displayed

    @allure.title('Проверка перехода на страницу авторизации')
    def test_check_redirect_to_sign_in(self, registration_page, generate_register_data):
        expected_url = Data.MAIN_PAGE_URL+Data.SIGN_IN_PAGE_URL
        _ = registration_page.create_account(generate_register_data)
        actual_url = registration_page.check_redirect_to_sign_in()
        assert expected_url == actual_url

    @pytest.mark.parametrize(
        "locator",
        (
                SignInPageLocators.EMAIL_FIELD,
                SignInPageLocators.PASSWORD_FIELD,
                SignInPageLocators.SIGN_IN_BUTTON
        )
    )
    @allure.title(f'Проверка, что в форме авторизации видно поле {"locator"}')
    def test_check_visible_sign_in_form(self, registration_page,generate_register_data, locator):
        registration_page.create_account(generate_register_data)
        assert registration_page.check_visible_sign_in_form(locator)
