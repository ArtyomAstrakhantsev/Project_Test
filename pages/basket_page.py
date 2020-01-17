from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BasketPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        basket_button.click()

    