import pytest
from selenium import webdriver

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

@pytest.mark.regression
def test_One(set_up):
    assert driver.title == "Google"

@pytest.mark.regression
def test_second(set_up):
    assert driver.title == "Google1"