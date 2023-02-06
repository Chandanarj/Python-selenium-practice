from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_MouseHover():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")

    driver.find_element(By.NAME, "username").send_keys("Test12")
    driver.find_element(By.NAME, "password").send_keys("Password")
    element_comment = driver.find_element(By.NAME, "comments")
    element_comment.clear()
    element_comment.send_keys("This is comments")
    driver.find_element(By.CSS_SELECTOR, '[name="checkboxes[]"][value="cb1"] ').click()

    radio_button2 = driver.find_element(By.CSS_SELECTOR, '[value="rd2"]')
    print(radio_button2.is_selected())

    radio_button1 = driver.find_element(By.CSS_SELECTOR, '[value="rd1"]')
    print(radio_button1.is_selected())
    radio_button1.click()

    
