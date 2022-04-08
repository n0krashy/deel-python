from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.fixedrate.fixed_rate_basic_page import FixedRateBasicPage


class ContractPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    FIXED_RATE_BUTTON = "h4=Fixed Rate"
    PAY_AS_YOU_GO_BUTTON = "h4=Pay As You Go"
    MILESTONE_BUTTON = "h4=Milestone"

    def get_fixed_rate_button(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.FIXED_RATE_BUTTON)

    def get_pay_as_you_go_button(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.PAY_AS_YOU_GO_BUTTON)

    def get_milestone_button(self):
        return self.wait_until_element_is_clickable(By.CSS_SELECTOR, self.MILESTONE_BUTTON)

    def get_page_url(self, url):
        return self.get_url(url)

    def click_fixed_rate(self):
        self.get_fixed_rate_button().click()
        return FixedRateBasicPage(self.driver)

    def click_milestone(self):
        self.get_milestone_button().click()
        return FixedRateBasicPage(self.driver)

    def click_pay_as_you_go(self):
        self.get_pay_as_you_go_button().click()
        return FixedRateBasicPage(self.driver)
