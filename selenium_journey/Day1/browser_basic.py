from selenium import webdriver
driver = webdriver.Chrome()
try:
    driver.get("https://www.google.com")
    print(driver.title)
    print(driver.current_url)
finally:
    driver.quit()