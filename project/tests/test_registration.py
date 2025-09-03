import allure
import pytest


class TestRegistration:

    @allure.title('Проверка регистрации')
    def test_registration(self, sign_in_page, registration_page, generate_register_data):
        sign_in_page.go_to_sign_in_page()
        registration_page.create_account(generate_register_data)
        condition_1 = registration_page.check_redirect_to_sign_in()
        condition_2 = sign_in_page.check_visible_sign_in_form()
        assert condition_1 == True and condition_2 == True
