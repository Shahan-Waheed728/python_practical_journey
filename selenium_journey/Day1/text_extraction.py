from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    element = driver.find_element(By.TAG_NAME,"h1")
    print(element.text)
finally:
    driver.quit()