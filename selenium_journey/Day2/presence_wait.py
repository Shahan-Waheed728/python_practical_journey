from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.TAG_NAME,"button")
    start_button.click()
    wait = WebDriverWait(driver,10)
    message = wait.until(
        EC.presence_of_element_located((By.ID,"finish"))
    )
    print(message.text)
finally:
    driver.quit()