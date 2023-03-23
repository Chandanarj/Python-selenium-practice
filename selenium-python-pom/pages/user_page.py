import time

from selenium.webdriver.common.by import By

from base_page import BasePage
from page_locators.user_locator import UserManagementLocator


class UserManagementPage(BasePage):

    def __init__(self, driver):
        self.userManagementLocator = UserManagementLocator()
        self.driver = driver

    def verify_breadcrumb(self, name_of_breadcrumb):
        header_breadcrumb = self.driver.find_element(*self.userManagementLocator.breadcrumb_header).text
        assert header_breadcrumb == name_of_breadcrumb

    def add_user(self, user_role, emp_name, emp_full_name, user_name, password):

        self.driver.find_element(*self.userManagementLocator.add_user_button).click()
        # User Role
        self.driver.find_element(*self.userManagementLocator.role_drop_down).click()
        self.driver.find_element(By.XPATH,
                                f'//*[@class="oxd-select-option"]/span[text()="{user_role}"]').click()

        # Employee Name
        self.driver.find_element(*self.userManagementLocator.employ_drop_down).send_keys(emp_name)
        time.sleep(10)
        self.driver.find_element(By.XPATH,
                                f"//*[text()='{emp_full_name}']").click()

        # Status
        self.driver.find_element().click(*self.userManagementLocator.status_drop_down)
        self.wait_and_click(*self.userManagementLocator.status_dropdown_value)
        #self.driver.find_element(*self.userManagementLocator.status_dropdown_value).click()

        # Username
        self.driver.find_element(*self.userManagementLocator.user_name_input).send_keys(user_name)

        # Password
        self.driver.find_element(*self.userManagementLocator.password_input).send_keys(password)

        # Confirm Password
        self.driver.find_element(*self.userManagementLocator.confirm_password_input).send_keys(password)

        # add button
        self.driver.find_element(*self.userManagementLocator.add_button).click()

    def verify_user_created(self, message):
        success_message = self.driver.find_element(self.userManagementLocator.toast_message).text
        assert success_message == message