import sys
sys.path.append('C:\\Users\\Marve\\OneDrive\\Документы\\Project_Test')
from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)    
    page.open()                      
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

def test_guest_can_auth(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_form()

def test_guest_can_register(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_registr_form()

def test_url_page_login(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_url()