from base_test import BaseTest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestDashboard(BaseTest):
    def test_verify_menu(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login_page = LoginPage(self.driver)
        login_page.login('admin', "admin123")

        login_page.verify_user_login('Paul Collings')

        dashboard_page = DashboardPage(self.driver)
        menus_actual = dashboard_page.capture_all_menus();
        menus_expected = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info',
                          'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz']
        assert menus_actual == menus_expected

        login_page.log_out()

    def test_verify_quick_launch_links(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        login_page.verify_user_login('Paul Collings')

        dashboard_page = DashboardPage(self.driver)
        links_actual = dashboard_page.capture_quick_launch_lists()
        link_expected = ['Assign Leave', 'Leave List', 'Timesheets',
                         'Apply Leave', 'My Leave', 'My Timesheet']
        assert  links_actual == link_expected
        login_page.log_out()




