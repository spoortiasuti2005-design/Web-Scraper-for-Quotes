# Web Scraper for Quotes

**Project Developed By: Spoorti Asuti**

## 1. Project Introduction

The Web Scraper for Quotes is a Python-based project that automatically collects quotes, author names, and tags from a publicly accessible website called [Quotes to Scrape](https://quotes.toscrape.com/).

Normally, when we want to collect information from a website, we need to open the website and copy the details manually. This project makes the process easier by using a Python program to automatically fetch and extract the required information.

The project uses the **Requests** library to connect to the website and download its webpage content. It uses **BeautifulSoup** to read and extract useful information from the HTML structure of the webpage.

The collected information is stored in a JSON file named `quotes.json`, which makes the data easy to read, manage, and reuse.

## 2. Project Objective

The main objectives of this project are:

- To understand how web scraping works using Python.
- To fetch webpage content using HTTP requests.
- To understand and inspect the HTML structure of a website.
- To extract quotes, author names, and tags automatically.
- To collect information from multiple pages.
- To store the extracted information in JSON format.
- To understand basic error handling and responsible web scraping.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Fetches webpage content |
| BeautifulSoup | Extracts information from HTML |
| JSON | Stores the extracted data |
| VS Code | Writing and running the program |

## 4. How Does the Project Work?

The project follows these steps:

1. **Connect to Website:** The Python program connects to Quotes to Scrape using the Requests library.
2. **Fetch Webpage:** It sends an HTTP GET request and receives the webpage content.
3. **Read HTML:** BeautifulSoup processes the HTML content.
4. **Find Quotes:** The program identifies quote containers using HTML selectors.
5. **Extract Information:** It extracts the quote text, author's name, and related tags.
6. **Multiple Pages:** It visits multiple pages and collects a maximum of 20 quotes.
7. **Save Data:** The collected information is stored in `quotes.json`.
8. **Display Result:** The program displays the collected author names and the total number of saved quotes.

## 5. Sample Output

When the program runs, the following output is displayed:

```text
===== WEB SCRAPER =====

Fetching page: 1
Collected: Albert Einstein
Collected: J.K. Rowling
Collected: Albert Einstein
Collected: Jane Austen
Collected: Marilyn Monroe
Collected: Albert Einstein
Collected: André Gide
Collected: Thomas A. Edison
Collected: Eleanor Roosevelt
Collected: Steve Martin

Fetching page: 2
Collected: Marilyn Monroe
Collected: J.K. Rowling
Collected: Albert Einstein
Collected: Bob Marley
Collected: Dr. Seuss
Collected: Douglas Adams
Collected: Elie Wiesel
Collected: Friedrich Nietzsche
Collected: Mark Twain
Collected: Allen Saunders

Total Quotes Saved: 20
Data saved successfully!

Scraping Completed!
```

## 6. Sample JSON Output

The extracted information is stored in a file called `quotes.json`.

Example:

```json
[
    {
        "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
        "author": "Albert Einstein",
        "tags": [
            "change",
            "deep-thoughts",
            "thinking",
            "world"
        ]
    },
    {
        "quote": "It is our choices, Harry, that show what we truly are, far more than our abilities.",
        "author": "J.K. Rowling",
        "tags": [
            "abilities",
            "choices"
        ]
    }
]
```

*Note: This is an illustrative sample of the JSON structure. The actual `quotes.json` file contains 20 collected records.*

## 7. Project Features

- Automatically collects quotes from a website.
- Extracts author names and related tags.
- Scrapes information from multiple webpages.
- Collects up to 20 records.
- Handles HTTP request errors.
- Uses a one-second delay between page requests.
- Saves extracted information in a structured JSON file.
- Avoids collecting private or login-protected information.

## 8. Project Folder Structure

```text
Web_Scraper_Quotes/
│
├── web_scraper.py
├── quotes.json
├── requirements.txt
└── README.md
```

- **web_scraper.py:** Contains the main Python scraping program.
- **quotes.json:** Stores the extracted quotes, authors, and tags.
- **requirements.txt:** Contains the required Python libraries.
- **README.md:** Provides project information and instructions.

## 9. How to Install and Run the Project

**Step 1: Install the required libraries**

```bash
pip install -r requirements.txt
```

**Step 2: Run the Python program**

```bash
python web_scraper.py
```

**Step 3: Check the result**

After successful execution, open `quotes.json` to view the collected quotes and their details.

## 10. Source Selection and Responsible Scraping

I selected [Quotes to Scrape](https://quotes.toscrape.com/) because it is a publicly accessible practice website designed for learning web scraping.

It provides quotes, author names, and tags without requiring a login. I used limited HTTP requests with a one-second delay between pages and avoided collecting private or personal information. I also considered the website's usage rules and scraping guidelines.

## 11. Learning Outcomes

Through this project, I learned:

- Basics of web scraping using Python.
- How HTTP GET requests work.
- How to fetch webpage content using Requests.
- How to inspect HTML elements.
- How to use BeautifulSoup selectors.
- How to extract text and attributes from HTML.
- How to handle request errors.
- How to save collected information in JSON format.
- The importance of responsible web scraping.

## 12. Conclusion

This project helped me understand how websites store information in HTML and how Python can automatically extract useful data from webpages.

By using Requests and BeautifulSoup, I successfully developed a simple web scraper that collects 20 quotes along with their authors and tags from multiple pages and stores the information in a JSON file.

This project improved my practical knowledge of Python, HTML parsing, data extraction, and file handling.

**Developed by: Spoorti Asuti**

**GitHub:** https://github.com/spoortiasuti2005-design
