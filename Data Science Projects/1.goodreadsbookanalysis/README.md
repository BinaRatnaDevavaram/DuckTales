# 📚 Goodreads Book Analysis — Python & Power BI Dashboard

This project analyzes the "Best Books Ever" list from Goodreads, combining Python and Power BI to uncover patterns in book ratings, popularity, and authorship.

> 📌 **Note:** All data was sourced from publicly accessible Goodreads pages and scraped using custom Python scripts strictly for **educational and non-commercial use**.
> ⚡ Unlike most projects that use a pre-cleaned Kaggle file, this one features a **custom dataset** scraped and processed entirely by me — almost **10,000 rows** of raw book data!

---

## 🎯 Project Goals

- Explore Goodreads' top-rated and most-rated books
- Compare how visualizations differ between Python (Matplotlib/Seaborn) and Power BI
- Build an end-to-end data pipeline and dashboard from raw scrape to insights

---

## 🧪 Process Overview

1. **Data Scraping**
   - Extracted book data from Goodreads' public list using Python & BeautifulSoup

2. **Data Cleaning**
   - Removed duplicates, fixed encoding, normalized author/title/genre
   - Filtered for books with >50K ratings to avoid niche rating distortions

3. **Exploratory Data Analysis EDA (Python)**
   - Created 6 Python charts to examine rating distributions, outliers, and trends

4. **Power BI Dashboard**
   - Replicated same 6 visuals in Power BI for comparison
   - Created multi-page dashboard with top authors, titles, and distributions

---

## 📊 Python vs Power BI Chart Comparisons

👉 Click to view: [`python_vs_powerbi_comparison.pdf`](screenshots/python_vs_powerbi_comparison.pdf)

---

## 🔍 Key Insights

- The highest-rated books tend to have fewer ratings — niche fandoms rate generously
- J.K. Rowling and Brandon Sanderson dominate both rating and count metrics
- Rating distributions are right-skewed — Goodreads users rate generously

---

## 🧠 What I Learned

- Working with web-scraped text data requires heavy cleanup before analysis
- Visual consistency across platforms (Python vs Power BI) requires attention to sorting, filters, and axes
- Building dashboards with a storytelling flow enhances understanding

---

## ⚙️ Installation & Tools

### 🐍 Python Setup

To install all required Python libraries for scraping, cleaning, visualizing, and exporting the final comparison:

```bash
pip install -r requirements.txt
```

## 📊 Power BI

- Power BI dashboards were built using Power BI Desktop (version: Aug 2023 or later).
- Download: [Power BI Desktop](https://powerbi.microsoft.com/desktop)

---

## 🗂️ Folder Structure

📁 1.goodreads-book-analysis/
├── data/
│ ├── goodreads_books_cleaned.csv
│ └── goodreads_books_scraped.csv
├── notebooks/
│ └── 01_scrape_goodreads.ipynb
│ └── 02_clean_explore.ipynb
│ └── 03_generate_comparisons.ipynb
├── power_bi/
│ └── goodreads_power_bi.pbix
├── python_charts/
├── screenshots/
│ ├── python/
│ ├── powerbi/
│ ├── comparisons/
│ └── python_vs_powerbi_comparison.pdf
├── scripts/
│ ├── scraper.py
│ ├── clean_explore.py
├── comparisons.py
├── requirements.txt
└── README.md

---

## 💬 Feedback

If you’ve got thoughts, questions, wild theories about Goodreads ratings, or epic book recommendations — I’m all ears (and eyes)! 📖✨

Drop a comment, open an issue, or just vibe with the code.

Crafted with caffeine and curiosity by 🐤 `DuckTales` — my coding alter ego.
Solving problems one quack at a time! 🦆💻
