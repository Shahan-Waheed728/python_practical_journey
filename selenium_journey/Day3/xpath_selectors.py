from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
try:
    driver.get("https://books.toscrape.com/index.html")
    wait = WebDriverWait(driver,20)
    books = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH,"//article[@class='product_pod']//h3//a"))
     )
    print("Title of all Books")
    for book in books:
        print(book.get_attribute("title"))
except TimeoutException:
    print("Timeout: The element was not found within 20 seconds.")
finally:
    driver.quit()