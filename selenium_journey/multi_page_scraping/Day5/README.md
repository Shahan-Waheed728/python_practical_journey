# Selenium Web Scraping Journey

A practical Python web-scraping project built using Selenium WebDriver. This project demonstrates browser automation, multi-page data extraction, record validation, CSV export, and data verification.

## Project Overview

The scraper collects book information from [Books to Scrape](https://books.toscrape.com/), a website designed for web-scraping practice.

Currently, the scraper processes the first three catalogue pages, collecting up to 60 book records.

## Features

- Automated Chrome browser navigation using Selenium
- Dynamic pagination using the Next button
- Explicit waits using `WebDriverWait`
- Book title, price, and availability extraction
- Validation of required fields
- Counting valid and invalid records
- CSV export using Python's built-in `csv` module
- Preservation of collected records when a Selenium timeout occurs
- CSV verification using `csv.DictReader`
- Automatic browser cleanup

## Project Structure

```text
Day5/
├── book_scraper.py
├── books.csv
└── README.md
```

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- Python CSV module

## Installation

Install Selenium:

```bash
pip install selenium
```

## How to Run

Run the main scraper:

```bash
python book_scraper.py
```

The program extracts book records, validates them, and exports the valid records to `books.csv`.

## Sample CSV Output

```csv
title,price,availability
A Light in the Attic,£51.77,In stock
```

## Expected Results

When all 60 records are valid:

```text
Page 1 completed.
Page 2 completed.
Page 3 completed.
Valid records: 60
Invalid records: 0
Total stored records: 60
Exported 60 books successfully.
Records read from csv: 60
CSV verification successful.
```

The CSV file contains 60 data rows plus one header row.

## Learning Outcomes

Through this project, I practiced:

1. Browser automation with Selenium.
2. CSS selectors and relative element extraction.
3. Dynamic pagination and explicit waits.
4. Python dictionaries and lists.
5. Data validation and error handling.
6. CSV file writing and reading.
7. Record-count verification.

## Next Improvements

- Export scraped data to JSON.
- Improve error handling and data-quality logging.
- Extend pagination beyond three pages.
- Add duplicate detection and stronger data verification.
- Refactor the scraper into reusable functions.

## Disclaimer

This project is for educational purposes and uses Books to Scrape, a website intended for scraping practice.