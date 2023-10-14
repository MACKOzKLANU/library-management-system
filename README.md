# Bookstore Management Program

This program allows you to manage books stored as data in a JSON file.

<h1>Avaiable commands: </h1>

- Read all books:
  - python3 utils.py read_json books.json
- Add a new book:
  - python3 utils.py add_book ISBN title description publish_year author price
- Filter books by maximum price:
  - python3 utils.py filter_maxprice books.json price
- Filter books by minimum price:
  - python3 utils.py filter_minprice books.json price
- Filter books by author:
  - python3 utils.py filter_author books.json author
- Filter books by minimum publication year:
  - python3 utils.py filter_minyear books.json publication_year
- Filter books by maximum publication year:
  - python3 utils.py filter_maxyear books.json publication_year


<h2>Usage Examples</h2>
Here are a few usage examples of the program(utils.py):
You can uncomment and use the sample function calls at the end of the script to test the functions and manage your book collection.

```python
# filter_maxprice("books.json", 50)
# filter_minprice("books.json", 30)
# filter_author("books.json", "author")
# filter_minyear("books.json", "2003")
# filter_maxyear("books.json", "2003")
# add_book(5464644, "name", "description", 2002, "author", 20)
# read_json("books.json")
```
