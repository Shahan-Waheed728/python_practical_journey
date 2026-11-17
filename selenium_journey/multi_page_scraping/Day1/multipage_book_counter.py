from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    total_books = 0
    wait = WebDriverWait(driver,10)
    for page in range(1,4):
        books = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod"))
        )
        print(f"Page {page}: {len(books)} books")
        total_books += len(books)
        if page < 3:
            next_page = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,".next a"))
            )
            previous_url = driver.current_url
            next_page.click()
            wait.until(
                EC.url_changes(previous_url)
            )
    print(f"Total books: {total_books}")
except TimeoutException:
    print("Page does not become visible in 10 seconds.")
finally:
    driver.quit()