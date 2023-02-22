import pytest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestOrangeHRMLogin(BaseTest):
    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        login_page.verify_user_login('Paul Collings')
        login_page.log_out()


