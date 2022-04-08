from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class FixedRateBasicPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    NAME_FIELD = "[name='name']"
    SCOPE_FIELD = "textarea[name='scope']"
    DEFAULT_STATE = 'div[data-qa="contractor-tax-residence-province"]'
    DEFAULT_COUNTRY = "div[data-qa='contractor-tax-residence'] div[class='deel-ui__select__input-container']"
    SUBMIT_BUTTON = "//button[@type='submit']"

    def get_name(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.NAME_FIELD)

    def get_scope(self):
        return self.wait_until_element_is_visible(By.CSS_SELECTOR, self.SCOPE_FIELD)

    def get_default_state(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.DEFAULT_STATE)

    def get_default_country(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.DEFAULT_COUNTRY)

    def get_submit_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUBMIT_BUTTON)

    def get_page_url(self, url):
        return self.get_url(url)

    def set_country(self, country):
        self.get_default_country().click()
        my_country = self.driver.find_element(By.CSS_SELECTOR, "div=" + country)
        my_country.click()

    def set_state(self, state):
        self.get_default_country().click()
        my_country = self.driver.find_element(By.CSS_SELECTOR, "div=" + state)
        my_country.click()

    def fill_mandatory_fields(self, name, country, state, scope):
        self.get_name().send_keys(name)
        self.set_country(country)
        self.set_state(state)
        self.get_scope().send_keys(scope)
        self.get_submit_button().click()

