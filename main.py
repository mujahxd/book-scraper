from scraper import get_all_books, save_to_csv, save_to_db, init_db

def main():
    all_books = get_all_books()
    save_to_csv(all_books)
    print(f"Scraped {len(all_books)} books and saved to books.csv!")
    save_to_db(all_books)
    

if __name__ == "__main__":
    init_db()
    main()