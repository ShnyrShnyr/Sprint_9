import allure

from project.data import Data


class TestSignIn:
    @allure.title("Проверка авторизации")
    def test_sign_in(self,sign_in_page, registration_page, recipes_page):
        registration_page.go_to_registration_page()
        registration_page.click_on_sign_in()
        sign_in_page.sign_in(Data.EMAIL, Data.PASSWORD)
        condition = recipes_page.check_redirect_to_recipes_page()
        assert condition == True
