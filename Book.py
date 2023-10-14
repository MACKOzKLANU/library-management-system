class Book:
    def __init__(self, ISBN, name, description, publish_year, author, price):
        self.ISBN = ISBN
        self.name = name
        self.description = description
        self.publish_year = publish_year
        self.author = author
        self.price = price
        
        
    def to_dict(self):
        return {
            "ISBN": self.ISBN,
            "name": self.name,
            "description": self.description,
            "publish_year": self.publish_year,
            "author": self.author,
            "price": self.price
        }