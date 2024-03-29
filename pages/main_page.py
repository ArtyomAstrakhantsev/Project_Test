from pages.base_page import BasePage
from locators.locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 
        return LoginPage(browser=self.browser, url=self.browser.current_url) 
    
    def should_be_login_link(self):
        assert self.is_element_present_login_link(*MainPageLocators.LOGIN_LINK), "Ссылка на страницу Логин отсутсвует на странице"