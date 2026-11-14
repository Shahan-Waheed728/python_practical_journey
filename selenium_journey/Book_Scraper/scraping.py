from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
print("=== Book Intelligence Report ===")
try:
    driver.get("https://books.toscrape.com/index.html")
    print("Website:",driver.title)
    wait = WebDriverWait(driver,10)
    books_a = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR,"article.product_pod"))
    )
    css_books = list(books_a)
    all_books_1 = []
    for book in css_books:
        title = book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR,".product_price p").text.strip()
        availability = book.find_element(By.CSS_SELECTOR,"p.instock.availability").text.strip()
        book_set_a = {
            "title" : title,
            "price" : price,
            "availability" : availability
        } 
        all_books_1.append(book_set_a)
    valid_count = 0
    invalid_count = 0
    for b in all_books_1:       
        if b["title"] and b["price"] and b["availability"]:
            valid_count += 1
        else:
            invalid_count += 1
    print(f"Valid records:{valid_count}")
    print(f"Invalid records: {invalid_count}")
    print("Extracted elements:",len(all_books_1))
   
    books_b = wait.until(
        EC.presence_of_all_elements_located((By.XPATH,"//article[@class='product_pod']"))
    )
    xpath_books = list(books_b)
    all_books_2 = []
    for book in xpath_books:
        title = book.find_element(By.XPATH,".//h3//a").get_attribute("title")
        price = book.find_element(By.XPATH,".//p[@class='price_color']").text.strip()
        availability = book.find_element(By.XPATH,".//p[@class='instock availability']").text.strip()
        book_set_b = {
            "title" : title,
            "price" : price,
            "availability" : availability
        } 
        all_books_2.append(book_set_b)
    v_count = 0
    iv_count = 0    
    for b in all_books_2:       
        if b["title"] and b["price"] and b["availability"]:
                v_count += 1
        else:
                iv_count += 1
    print(f"Valid records:{v_count}")
    print(f"Invalid records: {iv_count}")
    print("Extracted elements:",len(all_books_2))    
    prices = []
    for b in all_books_2:
        clean_price = b["price"].replace("£", "")
        price = float(clean_price)  
        prices.append(price)   
    exp_book = max(prices)  
    for b in all_books_2:
        cp = b["price"].replace("£", "")
        np = float(cp)
        if np == exp_book:
            print(f"Expensive book: {b['title']}") 
    print(f"Price: {exp_book}")
    seen_titles = set()
    duplicate_titles = []
    for book in all_books_2:
        title = book["title"]
        if title in seen_titles:
            duplicate_titles.append(title)
        else:
            seen_titles.add(title)
    print(f"Duplicate titles: {len(duplicate_titles)}")
    if (all_books_1 == all_books_2) and len(all_books_1) == 20 and len(all_books_2) == 20 and invalid_count == 0 and iv_count == 0 and len(duplicate_titles) == 0:
        print("CSS vs XPATH comparison: Match") 
        print("Scraping status: SUCCESS")  
    else:
        print("CSS vs XPATH comparison: Mismatch")
        print("Scraping status: FAILED")

except TimeoutException:
    print("Timeout: Books does not become visible at given time.")
finally:
    driver.quit()
    print("Browser closed successfully.")
