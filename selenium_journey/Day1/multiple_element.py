from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    elements = driver.find_elements(By.TAG_NAME,"label")
    for element in elements:
        print(element.text)
    print(len(elements))
finally:
    driver.quit()
