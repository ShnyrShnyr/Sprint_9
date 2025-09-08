import pytest
import random
import string
from selenium import webdriver
from project.pages.sign_in_page import SignInPage
from project.pages.recipes_page import RecipesPage
from project.pages.registration_page import RegistrationPage


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("browserVersion", "128.0")
    chrome_options.set_capability("selenoid:options", {
        "enableVNC": False,
        "enableVideo": False
    })
    drv = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub',
        options=chrome_options
    )
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
