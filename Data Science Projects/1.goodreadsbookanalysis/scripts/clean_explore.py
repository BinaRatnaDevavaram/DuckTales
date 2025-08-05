#-------------------------
# 📚 Import libraries
#-------------------------
# This script cleans and explores the Goodreads "Best Books Ever" dataset.
# It uses:
# pandas: for loading, cleaning, and manipulating data.
# matplotlib.pyplot: for making custom plots and visualizations.
# seaborn: for statistical visualizations (built on top of matplotlib).
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 📦 Load and Preview Data
# ----------------------------
def load_data(filepath):
    df = pd.read_csv(filepath)
    print("🔢 Dataset shape:", df.shape)
    print(df.head())
    return df


# ----------------------------
# 🧼 Clean Duplicates
# ----------------------------
def remove_duplicates(df):
    duplicates = df.duplicated().sum()
    print("\n🔍 Checking for duplicates...")
    if duplicates > 0:
        print(f"⚠️ Found {duplicates} duplicate rows. Removing them...")
        df = df.drop_duplicates()
    else:
        print("✅ No duplicate rows found.")
    return df

# ----------------------------
# 🧹 Handle Missing Data
# ----------------------------
def drop_missing(df):
    print("\n🧹 Checking for missing values...")
    missing = df.isnull().sum().sum()
    if missing > 0:
        print(f"⚠️ Found {missing} missing values. Dropping rows with missing 'Avg Rating' or 'Num Ratings'...")
        df = df.dropna(subset=['Avg Rating', 'Num Ratings'])
    else:
        print("✅ No missing values found.")
    return df

# ----------------------------
# 🔧 Convert Columns to Proper Types
# ----------------------------
def convert_types(df):
    df['Avg Rating'] = df['Avg Rating'].astype(float)
    df['Num Ratings'] = df['Num Ratings'].astype(int)
    return df

# ----------------------------
# 🧠 Basic Insights
# ----------------------------
def print_top_books(df):
    print("\n📊 Top 10 most rated books:")
    print(df.sort_values('Num Ratings', ascending=False).head(10)[['Title', 'Author', 'Avg Rating', 'Num Ratings']])

    print("\n🌟 Top 10 highest rated books (with >100k ratings):")
    popular = df[df['Num Ratings'] > 100000]
    print(popular.sort_values('Avg Rating', ascending=False).head(10)[['Title', 'Author', 'Avg Rating', 'Num Ratings']])

# ----------------------------
# 📊 Charts
# ----------------------------

# ----------------------------
# 📈 Chart 1: Distribution of Average Ratings
# Shows how average ratings are spread across all books
# ----------------------------
def plot_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Avg Rating'], bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Average Ratings')
    plt.xlabel('Average Rating')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 📈 Chart 2: Top 20 Most Rated Books
# Highlights books with the highest number of ratings
# ----------------------------
def plot_top_rated_books(df):
    top_rated = df.sort_values('Num Ratings', ascending=False).head(20)
    plt.figure(figsize=(10, 8))
    sns.barplot(data=top_rated, y='Title', x='Num Ratings', palette='viridis')
    plt.title('Top 20 Most Rated Books')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Book Title')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 📈 Chart 3: Top 20 Highest Rated Books (with >50k Ratings)
# Filters out obscure books and highlights high-rated popular ones
# ----------------------------
def plot_highest_rated_books(df):
    top_high = df[df['Num Ratings'] > 50000].sort_values('Avg Rating', ascending=False).head(20)
    plt.figure(figsize=(10, 8))
    sns.barplot(data=top_high, y='Title', x='Avg Rating', palette='coolwarm')
    plt.title('Top 20 Highest Rated Books (with >50k ratings)')
    plt.xlabel('Average Rating')
    plt.ylabel('Book Title')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 📈 Chart 4: Scatter Plot of Ratings vs. Average Score
# Examines if books with more ratings tend to get higher/lower scores
# ----------------------------
def plot_rating_scatter(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Num Ratings', y='Avg Rating', alpha=0.5)
    plt.title('Number of Ratings vs Average Rating')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Average Rating')
    plt.xscale('log')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 📈 Chart 5: Distribution of Rating Counts
# Shows how many books received few vs many ratings
# ----------------------------
def plot_rating_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Num Ratings'], bins=50, color='orange')
    plt.title('Distribution of Number of Ratings')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Count')
    plt.xscale('log')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 📈 Chart 6: Top 10 Most Frequent Authors
# Shows which authors appear most often on the list
# ----------------------------
def plot_top_authors(df):
    top_authors = df['Author'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_authors.values, y=top_authors.index, palette='magma')
    plt.title('Top 10 Most Frequent Authors in List')
    plt.xlabel('Number of Books')
    plt.ylabel('Author')
    plt.tight_layout()
    plt.show()

# ----------------------------
# 🚀 Main Runner - Run ALL Steps
# ----------------------------
def main():
    df = load_data('../data/goodreads_books_scraped.csv')
    df = remove_duplicates(df)
    df = drop_missing(df)
    df = convert_types(df)
    
    print_top_books(df)
    
    plot_distribution(df)
    plot_top_rated_books(df)
    plot_highest_rated_books(df)
    plot_rating_scatter(df)
    plot_rating_distribution(df)
    plot_top_authors(df)

    df.to_csv('../data/goodreads_books_cleaned.csv', index=False)
    print("\n✅ Cleaned data saved to: goodreads_books_cleaned.csv")

# 🔁 Run main if this file is executed directly
if __name__ == "__main__":
    main()
