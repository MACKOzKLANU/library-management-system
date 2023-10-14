import json
from Book import Book

def read_json(filename):
    #open file
    with open(filename, "r") as file:
        books = json.load(file)
        #print all books
        print("All Books:\n ")
        for book in books:
            print("ISBN:", book["ISBN"])
            print("Name:", book["name"])
            print("Description:", book["description"])
            print("Publish Year:", book["publish_year"])
            print("Author:", book["author"])
            print("Price:", book["price"],"\n")
    return books
            
def add_book(ISBN, name, description, publish_year, author, price):
    new_book = Book(ISBN, name, description, publish_year, author, price)
    #read from file
    with open("books.json", "r") as file:
        books = json.load(file)
        print(books)
    #create new book dictionary of book specific information
    books.append(new_book.to_dict())
    #save books to file
    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)
        
def filter_maxprice(filename, max_price):
    results = []
    with open(filename, "r") as file:
        books = json.load(file)
        print("All Books with price lower than: ", max_price, "\n")
        for book in books:
            if book["price"] < max_price:
                results.append(book)
                print("ISBN:", book["ISBN"])
                print("Name:", book["name"])
                print("Description:", book["description"])
                print("Publish Year:", book["publish_year"])
                print("Author:", book["author"])
                print("Price:", book["price"], "\n")
    
    if not results:
        print("No books with the given parameters")
    
    return results



def filter_minprice(filename, min_price):
    results = []
    with open(filename, "r") as file:
        books = json.load(file)
        print("All Books with price bigger than:", min_price, "\n")
        for book in books:
            if book["price"] > min_price:  # Changed '<' to '>'
                results.append(book)
                print("ISBN:", book["ISBN"])
                print("Name:", book["name"])
                print("Description:", book["description"])
                print("Publish Year:", book["publish_year"])
                print("Author:", book["author"])
                print("Price:", book["price"], "\n")
        if not results:
            print("No books with the given parameters")
    return results

def filter_author(filename, author):
    results = []
    with open(filename, "r") as file:
        books = json.load(file)
        
        for book in books:
            if book["author"] == author:
                results.append(book)
                print("ISBN:", book["ISBN"])
                print("Name:", book["name"])
                print("Description:", book["description"])
                print("Publish Year:", book["publish_year"])
                print("Author:", book["author"])
                print("Price:", book["price"], "\n")
    
    if not results:
        print("No books by the given author")
    
    return results


def filter_minyear(filename, minyear):
    results = []
    with open(filename, "r") as file:
        books = json.load(file)
        print("All Books  under:", minyear, "\n")
        for book in books:
            if int(book["publish_year"]) <= int(minyear):
                results.append(book)
                print("ISBN:", book["ISBN"])
                print("Name:", book["name"])
                print("Description:", book["description"])
                print("Publish Year:", book["publish_year"])
                print("Author:", book["author"])
                print("Price:", book["price"], "\n")
        if not results:
            print("No books with the given parameters")
    return results

def filter_maxyear(filename, maxyear):
    results = []
    with open(filename, "r") as file:
        books = json.load(file)
        print("All Books above:", maxyear, "\n")
        for book in books:
            if int(book["publish_year"]) >= int(maxyear):
                results.append(book)
                print("ISBN:", book["ISBN"])
                print("Name:", book["name"])
                print("Description:", book["description"])
                print("Publish Year:", book["publish_year"])
                print("Author:", book["author"])
                print("Price:", book["price"], "\n")
    
    if not results:
        print("no books with the given parameters")
    
    return results

       
#here you can manually run functions
         
# filter_maxprice("books.json", 50)
# filter_minprice("books.json", 30)

# filter_author("books.json", "author")

# filter_minyear("books.json", "2003")
# filter_maxyear("books.json", "2003")


# add_book(5464644, "name", "description", 2002, "author", 20)
# read_json("books.json")
