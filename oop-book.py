class Book:

    def __init__(self, title, author, isbn, price, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.is_available = is_available
        self.books = []
        self.count = 0
        self.dict = {self.title:self.price}


    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} ({status})"

class Library(Book):

    def add_book(self, new_book):
        self.books.append(new_book)
        print(f"Added: {new_book.title}")

    def borrow_book(self, search_title):
        for book in self.books:
            if book.title == search_title:
                if book.is_available:
                    book.is_available = False
                    print(f"Success! You borrowed {book.title}")
                    return
                else:
                    print("Sorry, that book is already checked out.")
                    return
        print("Book not found in our system.")

    def purchase_book(self, title):
        self.books.remove(title)
        print(f"{self.title} bought from the library, count:{self.count}")
        self.count += 1

    def get_price_by_book(self, title):
        for title, price in self.dict.items():
            if title == self.title:
                print(price)
