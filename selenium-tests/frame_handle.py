from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium_demo():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    #driver.get("https://the-internet.herokuapp.com/iframe")
    driver.get("https://the-internet.herokuapp.com/nested_frames")
    driver.implicitly_wait(10)

    driver.switch_to.frame("frame-top")
    driver.switch_to.frame("frame-left")
    left_frame = driver.find_element(By.TAG_NAME, "body").text
    print(left_frame)
    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame-middle")
    middle_frame = driver.find_element(By.ID, "content").text
    print(middle_frame)
    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame-right")
    right_frame = driver.find_element(By.TAG_NAME, "body").text
    print(right_frame)
    driver.switch_to.default_content()
    driver.switch_to.frame("frame-bottom")
    bottom_frame = driver.find_element(By.TAG_NAME, "body").text
    print(bottom_frame)



    #content = driver.find_element(By.CSS_SELECTOR, '[class="example"] h3').text
    #print(content)

    #driver.switch_to.frame(0)
    #element = driver.find_element(By.ID, "tinymce")
    #element.clear()
    #element.send_keys("Testing")

    #driver.switch_to.parent_frame()
    #content = driver.find_element(By.CSS_SELECTOR, '[class="example"] h3').text
    #print(content)