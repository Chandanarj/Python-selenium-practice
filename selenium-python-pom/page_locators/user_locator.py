from selenium.webdriver.common.by import By


class UserManagementLocator():
    breadcrumb_header = (By.CSS_SELECTOR, '[class="oxd-topbar-header-breadcrumb"]')
    add_user_button = (By.CSS_SELECTOR, '[class="oxd-icon bi-plus oxd-button-icon"]')
    role_drop_down = (By.XPATH, '//div[div[label[text()="User Role"]]]//div[@class="oxd-select-text-input"]')
    employ_drop_down = (By.XPATH, '//div[div[label[text()="Employee Name"]]]//input')
    status_drop_down = (By.XPATH, '//div[div[label[text()="Status"]]]/div[2]/div/div/div')
    status_dropdown_value = (By.XPATH, '//*[@class="oxd-select-option"]/span[text()="Enabled"]')
    user_name_input = (By.XPATH, '//div[div[label[text()="Username"]]]//input')
    password_input = (By.XPATH, '//div[div[label[text()="Password"]]]//input')
    confirm_password_input = (By.XPATH, '//div[div[label[text()="Confirm Password"]]]//input')
    add_button = (By.CSS_SELECTOR, '[class="oxd-form-actions"] > button:nth-child(3)')
    toast_message = (By.CSS_SELECTOR, '[class="oxd-toast-content oxd-toast-content--success"]')