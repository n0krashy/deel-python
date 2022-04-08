import pytest
import softest
from pages.login_page import LoginPage
from config.config import TestData


@pytest.mark.usefixtures("setup")
class TestFixedTermContract(softest.TestCase):
    def test_login(self):
        login_page = LoginPage(self.driver)
        home_page = login_page.login(TestData.EMAIL, TestData.PASSWORD)
        url = home_page.get_page_url(TestData.HOMEPAGE_URL)
        self.soft_assert(self.assertEqual, url, TestData.HOMEPAGE_URL)
        self.assert_all()
