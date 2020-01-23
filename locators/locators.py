from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_PRODUCT = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    NAME_PRODUCT_IN_MESSAGE_OF_SUCCESS = (By.XPATH, "//*[@id='messages']/div[1]/div/strong") #название продукта в блоке с сообщением
    PRICE_EQUAL_CART = (By.XPATH, "//*[@id='messages']/div[3]/div") #весь блок с сообщением
    NAME_PRODUCT = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1") #название продукта
    PRICE_PRODUCT = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]") #цена товара на странице товара
    PRICE_IN_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong") #цена товара в сообщении на странице товара