# Python Selenium Web Scraping Journey

A hands-on Python learning journey focused on browser automation, web scraping, dynamic content extraction, and building reliable automation tools using Selenium.

## Objectives

- Understand browser automation with Selenium WebDriver.
- Learn how to locate and interact with HTML elements.
- Extract structured information from webpages.
- Explore dynamic content, scrolling, and explicit waits.
- Build practical web scraping projects.

## Day 1 — Selenium Fundamentals

**Date:** November 7, 2026

### Topics Covered

- Browser initialization using Chrome WebDriver
- Navigating to websites
- Retrieving page titles and URLs
- Locating HTML elements using `By.NAME` and `By.TAG_NAME`
- Entering text using `send_keys()`
- Extracting visible text using `.text`
- Finding multiple elements using `find_elements()`
- Using `try...finally` for browser cleanup

### Practice Website

https://www.selenium.dev/selenium/web/web-form.html

## Day 2 — Dynamic Content and Explicit Waits

**Date:** November 8, 2026

### Topics Learned

- Understanding static and dynamically loaded webpage content
- Differences between `time.sleep()` and `WebDriverWait`
- Waiting for elements using `presence_of_element_located()`
- Waiting for visible elements using `visibility_of_element_located()`
- Understanding `TimeoutException`
- Handling failures using `try...except...finally`
- Ensuring browser cleanup with `driver.quit()`

### Practical Exercises

**Exercise 1: Waiting for Dynamic Elements**
- Opened Dynamic Loading Example 2.
- Clicked the Start button.
- Waited for the target element to appear in the DOM.
- Extracted the displayed message.

**Exercise 2: Waiting for Hidden Elements**
- Opened Dynamic Loading Example 1.
- Used `visibility_of_element_located()` to wait for initially hidden content.
- Extracted the text after the element became visible.

**Exercise 3: Timeout Exception Handling**
- Configured a two-second explicit wait.
- Handled `TimeoutException` using an exception handler.
- Ensured browser cleanup using `finally`.

### Key Learning

An element's presence in the DOM does not guarantee its visibility. Reliable browser automation requires choosing appropriate wait conditions and handling failures predictably.

### Next Milestone — Day 3

Extracting multiple elements from dynamic websites, handling missing data, and building a small practical scraper.

### Technologies

- Python
- Selenium
- Google Chrome
- VS Code

## Installation

```bash
python -m pip install -r requirements.txt
```

## Learning Philosophy

Understand → Implement → Test → Improve → Document.