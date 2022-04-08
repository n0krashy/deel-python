from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.home_page import HomePage


class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    EMAIL_FIELD = "#mui-1"
    PASSWORD_FIELD = "#mui-2"
    LOGIN_BUTTON = "button[type='submit']"

    def get_email_field(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.EMAIL_FIELD)

    def get_password_field(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.PASSWORD_FIELD)

    def get_login_button(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.LOGIN_BUTTON)

    def login(self, email, password):
        self.get_email_field().send_keys(email)
        self.get_password_field().send_keys(password)
        self.get_login_button().click()
        return HomePage(self.driver)

