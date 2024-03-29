from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locators.locators import MainPageLocators
from locators.locators import LoginPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():

    def __init__(self, browser, url, timeout=100):
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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")