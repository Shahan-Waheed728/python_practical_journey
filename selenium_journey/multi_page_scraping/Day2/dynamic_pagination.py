from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    wait = WebDriverWait(driver,10)
    page_count = 1
    while True:
        next_button = driver.find_elements(By.CSS_SELECTOR,".next a")
        if not next_button:
            print("Last page reached.")
            break
        previous_url = driver.current_url
        next_button[0].click()
        wait.until(
           EC.url_changes(previous_url)
        )
        page_count += 1
    print(f"Total pages visited: {page_count}")
       
except TimeoutException:
   print("Time-out error: Page does not become visible in 10 seconds.")
finally:
    driver.quit()