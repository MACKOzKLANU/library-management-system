import unittest
import json
from utils import read_json, add_book, filter_maxprice, filter_minprice, filter_author, filter_minyear, filter_maxyear

class TestBookMethods(unittest.TestCase):
    def test_read_json(self):
        # Test if read_json returns a list of dictionaries
        books = read_json("books.json")
        self.assertTrue(isinstance(books, list))
        for book in books:
            self.assertTrue(isinstance(book, dict))

    def test_add_book(self):
        # Test if add_book adds a book to the JSON file
        # You may need to replace these values with actual data
        ISBN = "1234567890"
        name = "Test Book"
        description = "Test description"
        publish_year = "2022"
        author = "Test Author"
        price = 25
        add_book(ISBN, name, description, publish_year, author, price)
        
        # Check if the book was added
        books = read_json("books.json")
        self.assertTrue(book["ISBN"] == ISBN for book in books)
    
    def test_filter_maxprice(self):
        # Test if filter_maxprice returns books with prices below the specified maximum
        max_price = 50
        result = filter_maxprice("books.json", max_price)
        for book in result:
            self.assertTrue(book["price"] < max_price)
    
    def test_filter_minprice(self):
        # Test if filter_minprice returns books with prices above the specified minimum
        min_price = 30
        result = filter_minprice("books.json", min_price)
        for book in result:
            self.assertTrue(book["price"] > min_price)
    
    def test_filter_author(self):
        # Test if filter_author returns books by a specific author
        author = "John Tren"  # Replace with an actual author from  data
        result = filter_author("books.json", author)
        for book in result:
            self.assertTrue(book["author"] == author)
    
    def test_filter_minyear(self):
        # Test if filter_minyear returns books published before the specified year
        min_year = "2010"
        result = filter_minyear("books.json", min_year)
        for book in result:
            self.assertTrue(int(book["publish_year"]) < int(min_year))
    
    def test_filter_maxyear(self):
        # Test if filter_maxyear returns books published after the specified year
        max_year = "2010"
        result = filter_maxyear("books.json", max_year)
        for book in result:
            self.assertTrue(int(book["publish_year"]) > int(max_year))

if __name__ == '__main__':
    unittest.main()
