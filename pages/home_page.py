from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.contract_page import ContractPage


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    COOKIES_DECLINE_BUTTON = "#CybotCookiebotDialogBodyButtonDecline"
    WHAT_IS_NEW_CLOSE_BUTTON = ".button.button-close"
    CREATE_NEW_CONTRACT_BUTTON = "p=Create A Contract"

    def get_cookies_decline_button(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.COOKIES_DECLINE_BUTTON)

    def get_what_is_new_close_button(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.WHAT_IS_NEW_CLOSE_BUTTON)

    def get_create_new_contract_button(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.CREATE_NEW_CONTRACT_BUTTON)

    def get_page_url(self, url):
        return self.get_url(url)

    def create_new_contract(self):
        self.get_cookies_decline_button().click()
        self.get_what_is_new_close_button().click()
        self.get_create_new_contract_button().click()
        return ContractPage(self.driver)

