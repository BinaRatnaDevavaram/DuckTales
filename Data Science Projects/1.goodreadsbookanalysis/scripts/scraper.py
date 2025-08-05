#-------------------------------------------------------------------
# 📚 Import necessary libraries
#-------------------------------------------------------------------
# This script scrapes the Goodreads "Best Books Ever" list and saves it to a CSV file.
# It uses:
# 📡 requests: Used to send HTTP requests to web pages and get the raw HTML response
# 🍜 BeautifulSoup: Parses HTML and XML documents, making it easy to extract data from web pages
# 📊 pandas: For storing, manipulating, and exporting structured data in DataFrame format
# ⏱️ time: Adds delays (like sleep) to avoid overloading servers or getting blocked
# 🗂️ os: Interacts with the operating system, such as creating folders or checking file paths
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# 📂 Ensure data folder exists
def create_data_folder(path='../data'):
    os.makedirs(path, exist_ok=True)
    
# 🌐 Generate the Goodreads list URL
def get_page_url(page_num):
    BASE_URL = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page={}"
    return BASE_URL.format(page_num)

# 🤖 Mimic a browser with headers
def get_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
            }
    

# 🧠 Extract book data from a BeautifulSoup row
def extract_book_data(row):
    try:
        title = row.find('a', class_='bookTitle').get_text(strip=True)
        author = row.find('a', class_='authorName').get_text(strip=True)
        rating_text = row.find('span', class_='minirating').get_text(strip=True)

        parts = rating_text.split(' — ')
        avg_rating = float(parts[0].split()[0])
        num_ratings = int(parts[1].split()[0].replace(',', ''))

        return {
            'Title': title,
            'Author': author,
            'Avg Rating': avg_rating,
            'Num Ratings': num_ratings
                }
    
    # If there are Exceptions and any data extraction fails, return None
    except Exception:
        return None


# 🕷️ Scrape a single page and return list of book dictionaries
def scrape_page(page_num):
    print(f"\n🔄 Scraping page {page_num} of 100...")
    url = get_page_url(page_num)
    response = requests.get(url, headers=get_headers())
    soup = BeautifulSoup(response.text, 'html.parser')
    book_rows = soup.find_all('tr', itemtype="http://schema.org/Book")
    print(f"📚 Found {len(book_rows)} books on page {page_num}")


    page_books = []
    for row in book_rows:
        book_data = extract_book_data(row)
        if book_data:
            page_books.append(book_data)

    # ⏱️ Be respectful to Goodreads
    time.sleep(2)  
    return page_books

# 🗃️ Main function to scrape all pages and save CSV
def scrape_goodreads_books(pages=100, output_path='../data/goodreads_books_scraped.csv'):
    create_data_folder()
    all_books = []

    for page in range(1, pages + 1):
        all_books.extend(scrape_page(page))

    df = pd.DataFrame(all_books)
    df.to_csv(output_path, index=False)
    print(f"\n✅ Scraping complete. Data saved to: {output_path}")


# ▶️ Run this script directly
if __name__ == "__main__":
    scrape_goodreads_books(pages=100)
