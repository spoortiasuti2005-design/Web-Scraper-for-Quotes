
# Web Scraper for Headlines & Quotes

## Project Description
This project is a Python-based web scraper that
collects quotes, author names and tags from a
public website using Requests and BeautifulSoup.

The extracted information is saved in a JSON file.

## Features
- Fetches webpage content using HTTP requests
- Extracts quotes using BeautifulSoup
- Collects author names and tags
- Scrapes multiple webpages
- Handles HTTP request errors
- Saves 20 records in JSON format

## Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON

## Installation

Install the required libraries:

pip install -r requirements.txt

## How to Run

Run the following command:

python web_scraper.py

## Data Source
https://quotes.toscrape.com/

This is a public practice website designed
for learning web scraping.

## Project Files
- web_scraper.py - Main Python program
- quotes.json - Scraped quote records
- requirements.txt - Required libraries
- README.md - Project documentation

## Learning Outcomes
- HTTP request handling
- HTML inspection
- BeautifulSoup selectors
- Data extraction
- JSON file handling
- Error handling


## Data Source
https://quotes.toscrape.com/

## Source Selection and Permission
I selected Quotes to Scrape (https://quotes.toscrape.com/) because it is a public practice website designed for learning web scraping. It provides publicly accessible quotes, authors and tags without requiring login.

I used limited HTTP requests with a one-second delay between pages and avoided collecting private or personal information. I also considered the website's usage rules and scraping guidelines.
