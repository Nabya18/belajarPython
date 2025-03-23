"""
# Magic Methods = Dunder methods (Double underscore) __init__, __str__, __add__, __len__, etc.
# They are automatically called by many of Python's built-in operations
# They allow developers to define or customize the behavior of the objects
"""

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __eq__(self, other): # equal, other = another object
        return self.title == other.title and self.author == other.author

    def __lt__(self, other): # less than
        return self.pages < other.pages

    def __gt__(self, other): # greater than
        return self.pages > other.pages

    def __add__(self, other): # addition
        return self.pages + other.pages

    def __contains__(self, keyword): # check if keyword is in the title
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key): # get the value of the key
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Key {key} was not found"

book1 = Book("Harry Potter", "JK Rowling", 500)
book2 = Book("Lord of the Rings", "JRR Tolkien", 1000)
book3 = Book("The Hobbit", "JRR Tolkien", 300)
book4 = Book("Harry Potter", "JK Rowling", 500)

print(book1) # Harry Potter by JK Rowling, 500 pages because of __str__ method
print(book1 == book4) # True because of __eq__ method
print(book2 > book3) # True because of __gt__ method
print(book1 + book4) # 1000 because of __add__ method
print("Harry" in book1) # True because of __contains__ method
print(book1["title"]) # Harry Potter because of __getitem__ method
print(book1["author"]) # JK Rowling because of __getitem__ method