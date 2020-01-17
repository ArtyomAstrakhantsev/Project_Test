from pages.base_page import BasePage
from locators.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_registr_form()

    def is_element_present_login_url(self, how, what):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Неверная ссылка на страницу Логина"

    def is_element_present_login_form(self, how, what):
        try:
            self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_form(self):
        assert self.is_element_present_login_form(*LoginPageLocators.LOGIN_FORM), "На странице Логин отсутствует форма авторизации"    

    def is_element_present_registr_form(self, how, what):
        try:
            self.browser.find_element(*LoginPageLocators.REGISTR_FORM)
        except NoSuchElementException:
            return False
        return True

    def should_be_registr_form(self):
        assert self.is_element_present_registr_form(*LoginPageLocators.REGISTR_FORM), "На странице Логин отсутствует форма регистрации"
    