# Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.

books = {}

def add_book(book):
    books[book] = True

def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book not available")

def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned")
    else:
        print("Book not found")

def search_book(book):
    if book in books:
        print("Book found")
    else:
        print("Book not found")

def display_books():
    for book in books:
        if books[book]:
            print(book)

add_book("Python")
add_book("Java")
add_book("C++")

issue_book("Python")
return_book("Python")
search_book("Java")
display_books()
