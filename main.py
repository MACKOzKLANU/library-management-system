import json
from utils import read_json, add_book, filter_maxprice, filter_minprice, filter_author, filter_minyear, filter_maxyear

def main():
    while True:
        print("Menu:")
        print("1. Display all books")
        print("2. Display books below a certain price")
        print("3. Display books above a certain price")
        print("4. Display books by a specific author")
        print("5. Display books published before a specific year")
        print("6. Display books published after a specific year")
        print("7. Add a new book")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            read_json("books.json")
        elif choice == "2":
            max_price = float(input("Enter the maximum book price: "))
            filter_maxprice("books.json", max_price)
        elif choice == "3":
            min_price = float(input("Enter the minimum book price: "))
            filter_minprice("books.json", min_price)
        elif choice == "4":
            author = input("Enter the book's author: ")
            filter_author("books.json", author)
        elif choice == "5":
            min_year = input("Enter the year before which books were published: ")
            filter_minyear("books.json", min_year)
        elif choice == "6":
            max_year = input("Enter the year after which books were published: ")
            filter_maxyear("books.json", max_year)
        elif choice == "7":
            ISBN = input("Enter ISBN: ")
            name = input("Enter title: ")
            description = input("Enter description: ")
            publish_year = input("Enter year of publication: ")
            author = input("Enter author: ")
            price = float(input("Enter price: "))
            add_book(ISBN, name, description, publish_year, author, price)
            print("The book has been added to the books.json file.")
        elif choice == "8":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
