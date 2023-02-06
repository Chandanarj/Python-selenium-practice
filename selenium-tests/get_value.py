from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("http://www.facebook.com")
    driver.implicitly_wait(10)
    title_text = driver.title
    print(title_text)
    assert title_text == 'Facebook – log in or sign up'

    #driver.find_element(By.XPATH, "//a[text()='Forgotten password?']").click()
    #current_url = driver.current_url
    #print(current_url)
    #assert 'from_login_screen=0' in current_url

    text_value = driver.find_element(By.TAG_NAME, "h2").text
    print(text_value)
    assert text_value == 'Facebook helps you connect and share with the people in your life.'

    attribute_value = driver.find_element(By.ID, "email").get_attribute("placeholder")
    print(attribute_value)
    assert attribute_value == 'Email address or phone number'

    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgotten password?").get_attribute("href")
    print(forgot_password_link)

    font_size  = driver.find_element(By.LINK_TEXT, "Forgotten password?").value_of_css_property("font-size")
    print(font_size)
