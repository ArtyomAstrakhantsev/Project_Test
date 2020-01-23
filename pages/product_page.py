from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT)
        basket_button.click()

    def should_be_product_page(self):
        self.should_be_message_of_success()
        self.should_be_price_equal_price_cart()
   
    def should_be_message_of_success(self):
        name_product_in_message_of_success = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE_OF_SUCCESS).text
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name_product == name_product_in_message_of_success, "Название товара не совпадает с сообщением об добавлении в корзину"

    def should_be_price_equal_price_cart(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert price_in_message == price_product, "Стоимость корзины не совпадает с ценой товара"

    

