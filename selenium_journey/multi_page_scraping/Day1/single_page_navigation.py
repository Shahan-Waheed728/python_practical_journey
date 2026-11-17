from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    print(f"Current url: {driver.current_url}")
    wait = WebDriverWait(driver,10)
    next_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,".next a"))
        )
    
    next_button.click()
    next_page = wait.until(
        EC.url_contains("page-2.html")
    )
    print(f"New url: {driver.current_url}")
except TimeoutException:
    print("Timeout-error: New url does not become visible in 10 seconds.")
finally:
    driver.quit()

