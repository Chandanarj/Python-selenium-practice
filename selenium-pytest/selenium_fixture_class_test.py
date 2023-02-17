import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_testrail.plugin import testrail, pytestrail


@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)   
    driver = webdriver.Chrome(options=options)    
    driver.implicitly_wait(10) 
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("set_up")
class BaseTest:
    pass


#@pytest.mark.skipif(sys.platform.startswith("win"), reason="Only for linux or Mac")
class TestSelenium_Demo(BaseTest):

    #@pytest.mark.xfail(sys.platform == "win32", reason="There are some defect in scenario and issue reported in Jira with ID")
    @pytest.mark.parametrize("search,exectedTitle", [("Testing1", "Testing1 - Google Search"), 
                                            ("Testing2", "Testing2 - Google Search")])
                                            #("Testing3", "Testing - Google Search")])
    def test_one(self, search, exectedTitle):
        
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"
        self.driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(search)
        self.driver.find_element(By.XPATH, '(//*[@value="Google Search"])[2]').click()
        assert self.driver.title == exectedTitle

    @pytestrail.case('C2431')
    def test_second(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google1"