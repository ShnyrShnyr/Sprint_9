import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)


    @allure.step("Поиск элемента с ожиданием пока не будет виден")
    def find_element_with_wait(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элемента в ДОМ")
    def find_element_with_wait_in_dom(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание пока модальное окно перестанет быть видимым")
    def waiting_to_invisible_element(self, locator):
        self.wait.until(ec.invisibility_of_element_located(locator))

    @allure.step("Переход по URL")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Ввести текст в поле ввода")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        text = element.text
        return text

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Проверить что элемент видимый')
    def check_element_visible(self, locator):
        element = self.find_element_with_wait(locator)
        return element.is_displayed()
