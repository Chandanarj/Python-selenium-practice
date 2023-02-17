import pytest
from base_test import BaseTest
from selenium.webdriver.common.by import By


class TestSelenium_Demo(BaseTest):

    @pytest.mark.parametrize("search,exectedTitle", [("Testing1", "Testing1 - Google Search"),
                                                     ("Testing2", "Testing2 - Google Search")])
    def test_one(self, search, exectedTitle):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(search)
        self.driver.find_element(By.XPATH, '(//*[@value="Google Search"])[2]').click()
        assert self.driver.title == exectedTitle


    def test_second(self):
        self.driver.get("https://facebook.com/")

        element = self.driver.find_element(By.ID, "email")
        element.clear()
        element.send_keys("Testing@gmail.com")

        element = self.driver.find_element(By.ID, "pass")
        element.clear()
        element.send_keys("Password")

        element = self.driver.find_element(By.NAME, "login")
        element.click()