from selenium import webdriver
from selenium.webdriver.common.by import By


def test_assertion_demo():
    assert 12 == 12
    assert "Test" in "Testing"

#Hard Assertion
#Soft Assertion

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("http://www.facebook.com")
    print(driver.get_window_size())
    driver.maximize_window()
    assert driver.title == "Facebook – log in"
    assert driver.find_element(By.ID, "email").get_attribute("placeholder") == "Email address or phone number"
    assert driver.find_element(By.ID, "pass").get_attribute("placeholder") == "Password"
    assert driver.find_element(By.NAME, "login").text == "Log in"
    element = driver.find_element(By.ID, "email")
    element.clear()
    element.send_keys("Test@gmail.com")

    element_pass = driver.find_element(By.ID, "pass")
    element_pass.clear()
    element_pass.send_keys("Password")

    login_button_element = driver.find_element(By.NAME, "login")
    login_button_element.click()

    #driver.quit()


