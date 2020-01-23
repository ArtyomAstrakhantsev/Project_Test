import sys
sys.path.append('C:\\Users\\Marve\\OneDrive\\Документы\\Project_Test')
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time


def test_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage (browser, url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_of_success()
    page.should_be_price_equal_price_cart()

def test_should_be_message_of_success(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage (browser, url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_of_success()

def test_should_be_price_equal_price_cart(browser):    
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage (browser, url)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_price_equal_price_cart()
