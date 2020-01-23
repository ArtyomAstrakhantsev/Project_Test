import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    browser = webdriver.Chrome(executable_path = "C:\\Users\\Marve\\OneDrive\\Документы\\Project_Test\\chromedriver.exe", chrome_options=chrome_options) 
    yield browser
    print("\nquit browser..")
    browser.quit()
