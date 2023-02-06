from selenium import webdriver
from selenium.webdriver.common.by import By

def test_take_screenshot():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.save_screenshot("screen.png")
    image_code = driver.get_screenshot_as_base64()
    print(image_code)

    element = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    element.screenshot("element.png")
    