import csv
import requests
from bs4 import BeautifulSoup
from scraper import BookScraper, BookModel, Session


def get_all_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        url = base_url.format(page)
        response = requests.get(url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        book_links = [a["href"] for a in soup.select(".product_pod h3 a")]
        if not book_links:
            break

        for link in book_links:
            full_link = BookScraper.BASE_URL + link
            scraper = BookScraper(full_link)
            book = scraper.scrape()
            if book:
                books.append(book)

        page += 1
    
    return books

def save_to_csv(books, filename="data/books.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Availability", "Rating", "Description", "UPC", "Product Type", "Price Excl Tax", "Price Incl Tax", "Tax", "Number of Reviews", "Book Link"])
        for book in books:
            writer.writerow([book.title, book.price, book.availability, book.rating, book.description, book.upc, book.product_type, book.price_excl_tax, book.price_incl_tax, book.tax, book.number_of_reviews, book.book_link])
        
def save_to_db(books):
    session = Session()
    try:
        for book in books:
            book_entry = BookModel(
                title=book.title,
                price=book.price,
                availability=book.availability,
                rating=book.rating,
                description=book.description,
                upc=book.upc,
                product_type=book.product_type,
                price_excl_tax=book.price_excl_tax,
                price_incl_tax=book.price_incl_tax,
                tax=book.tax,
                number_of_reviews=int(book.number_of_reviews),
                book_link=book.book_link
            )
            session.add(book_entry)

        session.commit()
        
        print(f"Saved {len(books)} books to database")
    except Exception as e:
        session.rollback()
        print(f"Error saving to database: {e}")
    finally:
        session.close()