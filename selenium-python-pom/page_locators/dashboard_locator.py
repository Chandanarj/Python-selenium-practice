from selenium.webdriver.common.by import By


class DashboardLocator():
    all_menus_element = (By.CSS_SELECTOR, "[class='oxd-main-menu'] > li > a > span")
    all_quick_launch_element = (By.CSS_SELECTOR, "div[class='orangehrm-quick-launch-heading'] > p")
    admin_menus_element = (By.XPATH, '//ul[@class="oxd-main-menu"]//a/span[text()="Admin"]')