# Day 3 — CSS Selectors and XPath

**Date:** November 9, 2026

## Learning Objectives

- Understand HTML DOM hierarchy.
- Learn CSS selectors and XPath expressions.
- Locate nested HTML elements.
- Extract multiple records from a webpage.
- Understand direct-child and descendant relationships.

## Practical Implementation

**Practice website:** https://books.toscrape.com/

### Exercise 1 — CSS Selectors

Used the following CSS selector to locate book title links:

```python
By.CSS_SELECTOR, ".product_pod h3 a"
```

Successfully extracted 20 book titles from the homepage.

### Exercise 2 — XPath

Used XPath to locate the same book title links:

```python
By.XPATH, "//article[@class='product_pod']//h3//a"
```

### Additional Concepts

- `find_elements()` retrieves multiple matching elements.
- `visibility_of_all_elements_located()` waits for matching elements to be visible.
- `get_attribute("title")` extracts the complete book title.
- CSS spaces and XPath `//` represent descendant relationships.
- CSS `>` and XPath `/` represent direct-child relationships.

## Key Learning

A reliable selector should identify the intended elements without depending unnecessarily on the entire HTML hierarchy.

## Next Milestone

Complete the Phase 1 practical assessment before beginning Phase 2: Structured Data Extraction.