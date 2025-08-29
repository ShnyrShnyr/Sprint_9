import allure
from selenium.webdriver.common.by import By

from page_object.data import Data
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec





class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента с ожиданием пока не будет виден")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(ec.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Поиск элемента с двойным ожиданием пока не будет виден")
    def find_element_with_long_wait(self, locator):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    @allure.step("Поиск элементов с ожиданием пока не будут видны все")
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(ec.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание пока модальное окно перестанет быть видимым")
    def waiting_to_invisible_element(self, locator):
        WebDriverWait(self.driver, Data.TIMEOUT).until(ec.invisibility_of_element_located(locator))

    @allure.step("Переход по URL")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Получить URL страницы")
    def get_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Ввести текст в поле ввода")
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step("Ввести текст в поле ввода и нажать ENTER")
    def add_text_to_element_with_enter(self,locator, text):
        self.find_element_with_wait(locator).send_keys(text + Keys.ENTER)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator):
        text = self.find_element_with_wait(locator).text
        return text

    @allure.step("Переключиться на другое окно")
    def switch_to_window(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step("Перетащить элемент в Chrome")
    def my_drag_and_drop(self, locator_from, locator_to):
        element_from = self.find_element_with_wait(locator_from)
        element_to = self.find_element_with_wait(locator_to)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_from, element_to).perform()

    @allure.step("Перетащить элемент в FireFox")
    def drag_and_drop_element(self, source_element, target_element):

        script = """
            function createEvent(type) {
                var event = new CustomEvent("CustomEvent");
                event.initCustomEvent(type, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(format, data) { this.data[format] = data; },
                    getData: function(format) { return this.data[format]; }
                };
                return event;
            }

            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                element.dispatchEvent(event);
            }

            function simulateHTML5DragAndDrop(source, target) {
                var dragStartEvent = createEvent('dragstart');
                dispatchEvent(source, dragStartEvent);

                var dropEvent = createEvent('drop');
                dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);

                var dragEndEvent = createEvent('dragend');
                dispatchEvent(source, dragEndEvent, dropEvent.dataTransfer);
            }

            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        src = self.find_element_with_wait(source_element)
        trg = self.find_element_with_wait(target_element)
        self.driver.execute_script(script, src, trg)

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Проверить что элемент видимый')
    def check_element_visible(self, locator):
        element = self.find_element_with_wait(locator)
        return element.is_displayed

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, Data.TIMEOUT).until(ec.element_to_be_clickable(locator))


    @allure.step('Авторизация без создания заказа')
    def auth_user_without_create_order(self):
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.EMAIL_FIELD)
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Авторизация с созданием заказа')
    def auth_user_create_order(self):
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)
        self.find_element_with_wait(LoginPageLocators.EMAIL_FIELD)
        self.add_text_to_element(LoginPageLocators.EMAIL_FIELD, Data.EMAIL)
        self.add_text_to_element_with_enter(LoginPageLocators.PASSWORD_FIELD, Data.PASSWORD)
        self.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
        if Data.BROWSER_NAME == 'Chrome':
            self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON, MainPageLocators.LOCATOR_TO)
            self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_2, MainPageLocators.LOCATOR_TO)
            self.my_drag_and_drop(MainPageLocators.INGREDIENT_ICON_3, MainPageLocators.LOCATOR_TO)
        else:
            self.switch_to_window()
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_ICON, MainPageLocators.LOCATOR_TO)
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_ICON_2, MainPageLocators.LOCATOR_TO)
            self.drag_and_drop_element(MainPageLocators.INGREDIENT_ICON_3, MainPageLocators.LOCATOR_TO)
        self.click_on_element(MainPageLocators.CREATE_ORDER_BUTTON)
        element = WebDriverWait(self.driver, Data.TIMEOUT).until(ec.visibility_of_element_located(MainPageLocators.CONFIRM_ORDER))
        order_number = self.get_text_from_element(MainPageLocators.CONFIRM_ORDER) # забираю текст из элемента
        return element, order_number

