import requests
from bs4 import BeautifulSoup
import json
import time

# Website URL
BASE_URL = "https://quotes.toscrape.com"

# Store all quotes
all_quotes = []

# Maximum quotes
MAX_QUOTES = 20

# Create HTTP session
session = requests.Session()

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0 (Educational Quote Scraper)"
}


# Scrape quotes from multiple pages
def scrape_quotes():

    page_number = 1

    while len(all_quotes) < MAX_QUOTES:

        url = f"{BASE_URL}/page/{page_number}/"

        print("\nFetching page:", page_number)

        try:
            response = session.get(
                url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print("Error:", error)
            break

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find quote containers
        quotes = soup.select("div.quote")

        if not quotes:
            print("No more quotes found.")
            break

        # Extract information
        for quote in quotes:

            quote_text = quote.select_one("span.text")
            author = quote.select_one("small.author")

            if quote_text is None or author is None:
                continue

            tags = quote.select("a.tag")

            quote_data = {
                "quote": quote_text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": [
                    tag.get_text(strip=True)
                    for tag in tags
                ]
            }

            all_quotes.append(quote_data)

            print("Collected:", author.get_text(strip=True))

            if len(all_quotes) >= MAX_QUOTES:
                break

        page_number += 1

        # Wait before next request
        if len(all_quotes) < MAX_QUOTES:
            time.sleep(1)


# Save quotes into JSON
def save_quotes():

    with open("quotes.json", "w", encoding="utf-8") as file:

        json.dump(
            all_quotes,
            file,
            indent=4,
            ensure_ascii=False
        )

    print("\nTotal Quotes Saved:", len(all_quotes))
    print("Data saved successfully!")


# Main function
def main():

    print("===== WEB SCRAPER =====")

    try:
        scrape_quotes()
        save_quotes()

    finally:
        session.close()

    print("\nScraping Completed!")


# Start program
if __name__ == "__main__":
    main()
