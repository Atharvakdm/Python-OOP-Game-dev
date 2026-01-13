class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} ({status})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

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


# 1. Create a book
b1 = Book("The Hobbit", "J.R.R. Tolkien", "12345")

# 2. Create the library
my_library = Library("City Central Library")

# 3. Add the book object to the library's list
my_library.add_book(b1)

# Now, my_library.books contains [b1]
print(my_library.books[0].title) # This would print: The Hobbit
