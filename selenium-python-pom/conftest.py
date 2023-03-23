import pytest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from MyListner import MyListner
from conf import Credential
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def set_up(request, browser_type):
    print("Running on brower : "+browser_type)
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'edge':
        driver = webdriver.Edge()
    driver.implicitly_wait(10)
    #driver = EventFiringWebDriver(driver, MyListner())
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser_type(request):
    return request.config.getoption("--browser")

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


