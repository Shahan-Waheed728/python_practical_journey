from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
def extract_book_data(book):      
    title = book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("title") or ""
    price = book.find_element(By.CSS_SELECTOR,".product_price p").text.strip()
    availability = book.find_element(By.CSS_SELECTOR,"P.instock.availability").text.strip()
    book_data = {
        "title" : title,
        "price" : price,
        "availability" : availability
    }  
    return book_data
def validate_book_data(book_info):
    title = book_info["title"]
    price = book_info["price"]
    availability = book_info["availability"]
    if title.strip() and price.strip() and availability.strip():
        return True
    else:
        return False
def go_to_next_page(driver,wait):
    next_button = driver.find_elements(By.CSS_SELECTOR,".next a")
    if not next_button:
        return False
    previous_url = driver.current_url
    next_button[0].click()
    wait.until(EC.url_changes(previous_url))
    return True
try:
    driver.get("https://books.toscrape.com/catalogue/page-1.html")
    wait = WebDriverWait(driver,10)
    all_books = []
    valid_records = 0
    invalid_records = 0
    page_count = 0
    while True:
        books = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod"))
        )       
        for book in books:
            book_info = extract_book_data(book)
            if validate_book_data(book_info):
                valid_records += 1
                all_books.append(book_info)
            else:
                print(f"Invalid: {book_info}")
                invalid_records += 1
        page_count +=1
        if page_count >= 3:
            print("Scraping job done successfully!")
            break
        if not go_to_next_page(driver,wait):
                break
    print(f"Valid records: {valid_records}")
    print(f"Invalid_records: {invalid_records}")
    print(f"Length of all books: {len(all_books)}")
except TimeoutException:
    print("Expected elements does not become visible in 10 seconds.")
finally:
    driver.quit()