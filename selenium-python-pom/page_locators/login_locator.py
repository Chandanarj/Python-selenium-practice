from selenium.webdriver.common.by import By


class LoginLocator():
    user_drop_down = (By.CSS_SELECTOR, "[class='oxd-userdropdown-name']")
    user_input = (By.NAME, "username")
    user_password = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button")
    logout_button = (By.XPATH, "//a[text()='Logout']")
    about_link = (By.XPATH, "//a[text()='About']")
    support_link = (By.XPATH, "//a[text()='Support']")