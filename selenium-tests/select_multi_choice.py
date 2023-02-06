from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.color import Color

def test_selenium_multi_choice():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
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
    #select.select_by_index(1)
    #select.select_by_index(2)
    select.deselect_by_index(3)

    print(select.is_multiple)
    
    
    print(Color.from_string('#00ff33').rgba)
    print(Color.from_string('rgb(1, 255, 3)').hex)
    print(Color.from_string('blue').rgba)
    print("==========================")