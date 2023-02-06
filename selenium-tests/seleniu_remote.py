from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color

def test_selenium_multi_choice():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Remote(
        command_executor="http://192.168.1.5:4444/wd/hub",
        options=webdriver.EdgeOptions()
    )

    #driver = webdriver.Chrome(options=options)
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
    driver.implicitly_wait(10)  

    driver.find_element(By.NAME, "username").send_keys("Test12")
    driver.find_element(By.NAME, "password").send_keys("Password")
    element_comment = driver.find_element(By.NAME, "comments")
    element_comment.clear()
    element_comment.send_keys("This is comments")
    driver.find_element(By.CSS_SELECTOR, '[name="checkboxes[]"][value="cb1"] ').click()  
  
    element = driver.find_element(By.CSS_SELECTOR, '[name="multipleselect[]"]')
    select = Select(element)
    select.select_by_value("ms2")
    select.select_by_value("ms3")