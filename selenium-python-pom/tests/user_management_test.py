from base_test import BaseTest

from pages.dashboard_page import DashboardPage
from pages.user_page import UserManagementPage


class TestUserManagement(BaseTest):
    def test_create_user(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.click_admin_menu()

        user_management_page = UserManagementPage(self.driver)
        user_management_page.verify_breadcrumb("Admin\nUser Management")

        user_management_page.add_user("Admin", "Paul Collings",
                                    'Paul Collings', "john.scot2433", "Password123@")
        # Verify user created
        user_management_page.verify_user_created("Success\nSuccessfully Saved")
