import pytest
import random
import string
from selenium import webdriver
from project.pages.sign_in_page import SignInPage
from project.pages.recipes_page import RecipesPage
from project.pages.registration_page import RegistrationPage
import os


'''def pytest_addoption(parser):
    parser.addoption(
        "--remote", action="store_true", default=False,
        help="Запускать в удалённом Selenoid (если не передан — локально)."
    )
    parser.addoption(
        "--selenoid-url", action="store", default="http://localhost:4444/wd/hub",
        help="URL удалённого Selenium (Selenoid)."
    )'''

@pytest.fixture(scope="function")
def driver(request):
    chrome_options = webdriver.ChromeOptions()

    if os.getenv('CI'):
        # --- РЕЖИМ Selenoid ---
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("browserVersion", "128.0")
        chrome_options.set_capability("selenoid:options", {
            "enableVNC": False,
            "enableVideo": False,
        })
        driver = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub",
            options=chrome_options
        )
    else:
        # --- ЛОКАЛЬНЫЙ РЕЖИМ ---
        # можно добавить любые аргументы, например:
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()


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
