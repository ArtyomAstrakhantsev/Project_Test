import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path = "C:\\Users\\Marve\\OneDrive\\Документы\\Project_Test\\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
