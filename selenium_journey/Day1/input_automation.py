from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    element = driver.find_element(By.ID,"my-text")
    element.send_keys("Learning Selenium with Python")
finally:
    driver.quit()