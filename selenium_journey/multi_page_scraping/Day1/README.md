## Selenium Pagination — Phase 2

### Task 1: Single-Page Navigation
- Located the Next button using the CSS selector `.next a`.
- Navigated from Page 1 to Page 2.
- Used explicit waits to verify successful navigation.
- Learned the difference between `driver.current_url` and `get_attribute("href")`.

### Task 2: Multi-Page Book Counting
- Implemented a `for` loop to navigate through three pages.
- Counted 20 books per page, totaling 60 books.
- Used `EC.url_changes()` to verify navigation.
- Applied a condition to prevent navigation beyond Page 3.
- Used `TimeoutException` for error handling and `finally` for browser cleanup.

**Next milestone:** Dynamic pagination without hardcoding the number of pages.