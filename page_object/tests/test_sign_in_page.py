import allure

from page_object.data import Data


class TestSignInPage:

    @allure.title("Проверить нажатие на кнопку войти со страницы регистрации")
    def test_click_on_sign_in(self, registration_page):
        element = registration_page.click_on_sign_in()
        assert element.is_displayed

    @allure.title("Проверить, что после авторизации отображается элемент выход")
    def test_sign_in(self, sign_in_page):
        element = sign_in_page.sign_in()
        assert element.is_displayed

    @allure.title("Проверить, что переходит на главную страницу с рецептами")
    def test_redirect_to_recipes(self, sign_in_page):
        expected_url = Data.MAIN_PAGE_URL+Data.RECIPES_URL
        _ = sign_in_page.sign_in()
        actual_url = sign_in_page.check_redirect_to_recipes()
        assert expected_url == actual_url




