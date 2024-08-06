import pytest
from selenium import webdriver
from conf import Credential
from pages.login_page import LoginPage

@pytest.fixture(scope="class")
def set_up(request, browser_type):
    print("Running on browser: " + browser_type)
    if browser_type == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'firefox':
        driver = webdriver.Firefox()
    elif browser_type == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser type: {browser_type}")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="class", autouse=True)
def browser_type(request):
    return request.config.getoption("--browser", default="chrome")

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
