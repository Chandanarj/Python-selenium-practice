from base_page import BasePage
from page_locators.dashboard_locator import  DashboardLocator


class DashboardPage(BasePage):

    def __init__(self, driver):
        self.dashboard_locator = DashboardLocator()
        self.driver = driver

    def capture_all_menus(self):
        return self.find_all_element_text(*self.dashboard_locator.all_menus_element)

    def capture_quick_launch_lists(self):
        elements = self.driver.find_elements(*self.dashboard_locator.all_quick_launch_element)
        links_actual = []
        for element in elements:
            links_actual.append(element.text)
        return links_actual

    def click_admin_menu(self):
        self.driver.find_element(*self.dashboard_locator.admin_menus_element).click()