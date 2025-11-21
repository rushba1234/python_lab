

class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)       # Base class constructor invoked
        self.title = title
        self.author = author

    # method overloading (same method name)
    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    # method overloading again
    def display(self):
        super().display()
        print("Price:", self.price)
        print("Pages:", self.pages)


# ---- main program ----
pname = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Price: "))
pages = int(input("Enter Number of Pages: "))

book1 = Python(pname, title, author, price, pages)

print("\n--- Python Book Information ---")
book1.display()

