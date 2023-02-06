from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_MouseClick():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    #driver.get("https://demoqa.com/droppable")
    driver.get("https://demoqa.com/dragabble")
    
    action =  ActionChains(driver)
    element = driver.find_element(By.ID, "dragBox")
    action.drag_and_drop_by_offset(element, 0, 100).perform()

    #element_source = driver.find_element(By.ID, "draggable")
    #element_target = driver.find_element(By.ID, "droppable")

    #action.drag_and_drop(element_source, element_target).perform()

    #element1 = driver.find_element(By.ID, "doubleClickBtn")
    #action.double_click(element1).perform()
    #element2 = driver.find_element(By.ID, "rightClickBtn")
    #action.context_click(element2).perform()
    #element3 = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    #action.click(element3).perform()
    #action.double_click(element1).pause(1).context_click(element2).pause(1).click(element3).perform()
    
