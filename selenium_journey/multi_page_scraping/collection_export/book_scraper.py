from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    wait = WebDriverWait(driver,10)
    all_books = []
    page_count = 1
    valid_records = 0
    invalid_records = 0
    while True:
        books = wait.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod"))
        )
        for book in books:
            title = book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("title")
            price = book.find_element(By.CSS_SELECTOR,".product_price p").text.strip()
            availability = book.find_element(By.CSS_SELECTOR,"p.instock.availability").text.strip()
            book_data = {
                "title" : title,
                "price" : price,
                "availability" : availability
            }
            if title.strip() and price.strip() and availability.strip():
                valid_records += 1
                all_books.append(book_data)
            else:
                invalid_records += 1
        print(f"Page {page_count} completed.")  
        if page_count == 3:
            break 
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
    print(f"Valid records: {valid_records}")
    print(f"Invalid records: {invalid_records}")
    print(f"Total stored records: {len(all_books)}")
except TimeoutException:
    print("Time-out error: Expected element does not become visible in 10 seconds.")   
finally:
    driver.quit()
