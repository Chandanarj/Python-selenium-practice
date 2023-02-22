from base_test import BaseTest
from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.user_page import UserManagementPage


class UserManagement:
    pass


class TestUserManagement(BaseTest):
    def test_create_user(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")
        login_page.verify_user_login('Paul Collings')
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_admin_menu()

        user_management_page = UserManagementPage(self.driver)
        user_management_page.verify_breadcrumb("Admin\nUser Management")

        user_management_page.add_user("Admin", "Paul",
                                    'Paul Collings', "john.scot2433", "Password123@")

        # Verify user created
        user_management_page.verify_user_created("Success\nSuccessfully Saved")

        login_page.log_out()





