from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, by, item):
        self.driver.find_element(by, item).click()

    def wait_and_click(self, by, item, time_out=10):
        element = WebDriverWait(self.driver, time_out)\
            .until(EC.presence_of_element_located(by, item))
        element.click()

    def enter_text(self, by, item, text):
        self.driver.find_element(by, item).send_keys(text)

    def clear_text(self, by, item):
        self.driver.find_element(by, item).clear()

    def clear_and_input_text(self, by, item, text):
        self.clear_text(by, item)
        self.enter_text(text)

    def get_text(self,by, item):
        return self.driver.find_element(by, item).text

    def get_attribute(self,by, item, attribute_name):
        return self.driver.find_element(by, item).get_attribute(attribute_name)

    def find_element(self,by, item):
        return self.driver.find_element(by, item)

    def find_elements(self, by, item):
        return self.driver.find_elements(by, item)

    def find_all_element_text(self, by, item):
        elements = self.find_elements(by, item)
        actual_list = []
        for element in elements:
            actual_list.append(element.text)
        return actual_list


