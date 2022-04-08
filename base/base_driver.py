from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(expected_conditions.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(expected_conditions.visibility_of_element_located((locator_type, locator)))
        return element

    def get_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
        return self.driver.current_url
