from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

def test_selenium_multi_choice():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.get("https://testpages.herokuapp.com/styled/attributes-test.html")
    driver.implicitly_wait(10)  

    element = driver.find_element(By.CSS_SELECTOR, '[class="styled-click-button"]')
    background_color = element.value_of_css_property("background-color")
    color = element.value_of_css_property("color")
    print(background_color)
    print(color)

    hex_background_color = Color.from_string(background_color).hex
    hex_color = Color.from_string(color).hex
    print(hex_background_color)
    print(hex_color)


    
