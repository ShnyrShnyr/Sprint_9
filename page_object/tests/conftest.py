import pytest
import random
import string

from selenium import webdriver

from page_object.data import Data
from page_object.pages.recipes_page import RecipesPage
from page_object.pages.registration_page import RegistrationPage
from page_object.pages.sign_in_page import SignInPage


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()

@pytest.fixture
def registration_page(driver):
    page = RegistrationPage(driver)
    page.go_to_url(Data.MAIN_PAGE_URL+Data.SIGN_UP_PAGE_URL)
    return page

@pytest.fixture
def sign_in_page(driver):
    page = SignInPage(driver)
    page.go_to_url(Data.MAIN_PAGE_URL+Data.SIGN_IN_PAGE_URL)
    return page

@pytest.fixture
def recipes_page(driver):
    page = RecipesPage(driver)
    page.go_to_url(Data.MAIN_PAGE_URL+Data.RECIPES_PAGE_URL)
    return page

@pytest.fixture
def generate_register_data():
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    register_data = {
        'firstname': generate_random_string(5),
        'lastname': generate_random_string(5),
        'username': generate_random_string(5),
        'email': f'{generate_random_string(5)}@mail.ru',
        'password': generate_random_string(8)
    }
    return register_data
