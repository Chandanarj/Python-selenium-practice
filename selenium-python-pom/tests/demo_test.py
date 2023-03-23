import pytest
from base_test import BaseTest
from selenium.webdriver.common.by import By
from pytest_testrail.plugin import testrail, pytestrail


class Selenium_Demo(BaseTest):

    #@pytestrail.case('C2516')
    #@pytest.mark.parametrize("search,exectedTitle", [("Testing1", "Testing - Google Search")])
    def test_one(self, search, exectedTitle):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(search)
        self.driver.find_element(By.XPATH, '(//*[@value="Google Search"])[2]').click()
        assert self.driver.title == exectedTitle

    #@pytestrail.case('C2517')
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