import requests
from bs4 import BeautifulSoup
from scraper import Book


class BookScraper:
    BASE_URL = "https://books.toscrape.com/"

    def __init__(self):
        self.books = []

    def fetch_page(self, url):
        """Mengambil halaman HTML dari URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
        
    def parse_book(self, book):
        """Mengekstrak informasi buku dari HTML."""
        title = book_html.h3.a.get("title")
        price = book_html.select_one(".price_color").text.strip()
        rating_class = book_html.select_one(".star-rating").get("class", [])
        rating = self.extract_rating(rating_class)
        availability = book_html.select_one(".availability").text.strip()
        product_page_url = self.BASE_URL + book_html.h3.a.get("href")
        
        return Book(
            title=title,
            price_excl_tax=0.0,  # Akan diperbarui nanti dari halaman detail
            price_incl_tax=0.0,
            tax=0.0,
            rating=rating,
            availability=availability,
            image_url="",  # Akan diperbarui nanti
            category="",   # Akan diperbarui nanti
            description="", # Akan diperbarui nanti
            upc="",          # Akan diperbarui nanti
            product_page_url=product_page_url,
            num_reviews=0     # Akan diperbarui nanti
        )
    
    def extract_rating(self, rating_class):
        """Mengubah teks rating menjadi angka (1-5)."""
        ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        for key in ratings:
            if key in rating_class:
                return ratings[key]
        return 0

    def scrape_books(self):
        """Scraping daftar buku dari halaman utama."""
        html = self.fetch_page(self.BASE_URL)
        if not html:
            return
        
        soup = BeautifulSoup(html, "html.parser")
        books_html = soup.select(".product_pod")
        
        for book_html in books_html:
            book = self.parse_book(book_html)
            self.books.append(book)
        
        print(f"Scraped {len(self.books)} books from main page.")