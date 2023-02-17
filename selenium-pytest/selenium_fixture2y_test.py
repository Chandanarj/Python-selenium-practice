import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_testrail.plugin import testrail, pytestrail


@pytest.fixture
def set_up():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Chrome(options=options)
    driver.get("https://google.com")
    driver.implicitly_wait(10)
    yield
    driver.quit()


@pytest.mark.smoke
@pytest.mark.regression
@pytestrail.case('C2433')
@pytest.mark.parametrize("SearchText", ["Testing1", "Testing2"])
def test_One(set_up, SearchText):
    assert driver.title == "Google"
    driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys(SearchText)
    driver.find_element(By.XPATH, '(//*[@name="btnK"])[2]')

@pytest.mark.regression
def test_second(set_up):
    assert driver.title == "Google1"