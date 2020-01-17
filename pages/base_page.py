from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locators.locators import MainPageLocators
from locators.locators import LoginPageLocators

class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present_login_link(self, how, what):
        try:
            self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present_login_link(*MainPageLocators.LOGIN_LINK), "Ссылка на страницу Логин отсутсвует на странице"
