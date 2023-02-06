from selenium import webdriver
from selenium.webdriver.common.by import By

def test_execute_js_code():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/download")
    driver.implicitly_wait(10)

    driver.find_element(By.LINK_TEXT, "titleSS.png").click()

    #element = driver.find_element(By.ID, "file-upload")
    #element.send_keys("C:\\Users\\admin\\Documents\\titleSS.png")
    #driver.find_element(By.ID, "file-submit").click()
    ##message = driver.find_element(By.TAG_NAME, "h3").text
    #assert message == "File Uploaded!"

     