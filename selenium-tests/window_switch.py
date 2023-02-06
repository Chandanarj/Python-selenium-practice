from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_execute_js_code():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=options)   
    driver.get("https://the-internet.herokuapp.com/windows")

    driver.find_element(By.LINK_TEXT, "Click Here").click()
    
    parent_winId = driver.current_window_handle
    list_winId = driver.window_handles
    for win_id in list_winId:
        driver.switch_to.window(win_id)
    
    text = driver.find_element(By.CSS_SELECTOR, '[class="example"] h3').text
    print(text)
    driver.close()
    driver.switch_to.window(parent_winId)
    text = driver.find_element(By.CSS_SELECTOR, '[class="example"] h3').text
    print(text)
    driver.quit()
    


