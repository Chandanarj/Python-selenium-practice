import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from MyListner import MyListner
from conf import Credential
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def set_up(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    #driver = EventFiringWebDriver(driver, MyListner())
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def navigate_url(request):
    request.cls.driver.get(Credential["Url"])


@pytest.fixture()
def login_logout(request):
    login_page = LoginPage(request.cls.driver)
    login_page.login(Credential['User'], Credential['Password'])
    login_page.verify_user_login(Credential['UserName'])
    yield
    login_page.log_out()


