import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from MyListner import  MyListner


@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver = EventFiringWebDriver(driver, MyListner())
    request.cls.driver = driver
    yield
    driver.quit()
