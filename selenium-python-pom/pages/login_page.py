from page_locators.login_locator import LoginLocator


class LoginPage():

    def __init__(self, driver):
        self.loginLocator = LoginLocator()
        self.driver = driver

    def login(self, user_name, password):
        self.driver.find_element(*self.loginLocator.user_input).send_keys(user_name)
        self.driver.find_element(*self.loginLocator.user_password).send_keys(password)
        self.driver.find_element(*self.loginLocator.login_button).click()

    def verify_user_login(self, user_name):
        user_name = self.driver.find_element(*self.loginLocator.user_drop_down).text
        assert user_name == user_name

    def log_out(self):
        self.driver.find_element(*self.loginLocator.user_drop_down).click()
        self.driver.find_element(*self.loginLocator.logout_button).click()

    def click_on_about(self):
        self.driver.find_element(*self.loginLocator.user_drop_down).click()
        self.driver.find_element(*self.loginLocator.about_link)

    def click_on_support(self):
        self.driver.find_element(*self.loginLocator.user_drop_down).click()
        self.driver.find_element(*self.loginLocator.support_link)