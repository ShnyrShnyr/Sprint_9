import pytest
import random
import string

from selenium import webdriver
from project.pages.sign_in_page import SignInPage
from project.pages.recipes_page import RecipesPage
from project.pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    yield drv
    drv.quit()

@pytest.fixture
def registration_page(driver):
    page = RegistrationPage(driver)
    return page

@pytest.fixture
def sign_in_page(driver):
    page = SignInPage(driver)
    return page

@pytest.fixture
def recipes_page(driver):
    page = RecipesPage(driver)
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
