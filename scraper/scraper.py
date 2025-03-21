from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

@dataclass
class Book:
    title: str
    price: str
    availability: str
    rating: str
    description: str
    upc: str
    product_type: str
    price_excl_tax: str
    price_incl_tax: str
    tax: str
    number_of_reviews: int
    book_link: str
class BookScraper:
    BASE_URL = "https://books.toscrape.com/catalogue/"

    def __init__(self, url: str):
        self.url = url
        self.soup = None

    def fetch_page(self):
        """Fetch the page content and parse it with BeautifulSoup."""
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            response.encoding = 'utf-8'  # Pastikan encoding diatur ke UTF-8
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page: {e}")
            self.soup = None

    def get_title(self):
        try:
            return self.soup.select_one("div.col-sm-6.product_main > h1").get_text(strip=True)
        except AttributeError:
            return "Title not found"
        
    def get_price(self):
        try:
            return self.soup.select_one("div.col-sm-6.product_main > p.price_color").get_text(strip=True)
        except AttributeError:
            return 0
        
    def get_availability(self):
        try:
            return self.soup.select_one("div.col-sm-6.product_main > p.instock.availability").get_text(strip=True)
            # return self.extract_stock(text)
        except AttributeError:
            return "Out of stock"

    def get_rating(self):        
        rating = self.soup.select_one("div.col-sm-6.product_main > p.star-rating")
        if rating:
            return rating["class"][1]
        return "No rating"
    
    def get_description(self):
        try:
            return self.soup.select_one("#product_description + p").get_text(strip=True)
        except AttributeError:
            return "No description"
    
    def get_table_data(self, index: int):
        try:
            return self.soup.select("table tr td")[index].get_text(strip=True)
        except (AttributeError, IndexError):
            return "Data not found"

    def get_upc(self):
        return self.get_table_data(0)
    
    def get_product_type(self):
        return self.get_table_data(1)
    
    def get_price_excl_tax(self):
        return self.get_table_data(2)

    def get_price_incl_tax(self):
        return self.get_table_data(3)
    
    def get_tax(self):
        return self.get_table_data(4)
    
    def get_number_of_reviews(self):
        return self.get_table_data(6)
    
    # def get_price_excl_tax(self):
    #     return self.clean_price(self.get_table_data(2))

    # def get_price_incl_tax(self):
    #     return self.clean_price(self.get_table_data(3))

    # def clean_price(self, price_text):
    #     return price_text.replace("£", "").strip()

    # def get_tax(self):
    #     return self.clean_price(self.get_table_data(4))

    # def get_price_excl_tax(self):
    #     return self.get_table_data(2)

    # def get_price_incl_tax(self):
    #     return self.get_table_data(3)
    
    # def get_tax(self):
    #     return self.get_table_data(4)

    # def extract_stock(self, availability_text):
    #     match = re.search(r"\d+", availability_text)  # Cari angka dalam teks
    #     return int(match.group()) if match else 0
    
    
    
    def scrape(self):
        """Run the scraping process."""
        self.fetch_page()
        if not self.soup:
            return None
        
        return Book(
            title=self.get_title(),
            price=self.get_price(),
            availability=self.get_availability(),
            rating=self.get_rating(),
            description=self.get_description(),
            upc=self.get_upc(),
            product_type=self.get_product_type(),
            price_excl_tax=self.get_price_excl_tax(),
            price_incl_tax=self.get_price_incl_tax(),
            tax=self.get_tax(),
            number_of_reviews=self.get_number_of_reviews(),
            book_link=self.url
        )