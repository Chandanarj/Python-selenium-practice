from page_locators.login_locator import LoginLocator
from base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.loginLocator = LoginLocator()
        self.driver = driver

    def login(self, user_name, password):
        self.enter_text(*self.loginLocator.user_input, user_name)
        self.enter_text(*self.loginLocator.user_password, password)
        self.click_on(*self.loginLocator.login_button)

    def verify_user_login(self, user_name):
        user_name = self.get_text(*self.loginLocator.user_drop_down)
        assert user_name == user_name

    def log_out(self):
        self.click_on(*self.loginLocator.user_drop_down)
        self.click_on(*self.loginLocator.logout_button)

    def click_on_about(self):
        self.click_on(*self.loginLocator.user_drop_down)
        self.click_on(*self.loginLocator.about_link)

    def click_on_support(self):
        self.click_on(*self.loginLocator.user_drop_down)
        self.click_on(*self.loginLocator.support_link)