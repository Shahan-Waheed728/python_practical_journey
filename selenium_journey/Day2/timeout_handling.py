from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = driver.find_element(By.TAG_NAME,"button")
    start_button.click()
    wait = WebDriverWait(driver,2)
    message = wait.until(
        EC.visibility_of_element_located((By.ID,"finish"))
    )
    print(message.text)
except TimeoutException:
    print("Timeout: The element with ID 'finish' was not visible within 2 seconds.")

finally:
    driver.quit()