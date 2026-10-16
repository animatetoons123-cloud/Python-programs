books = []


def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author: ")

    books.append([book_id, title, author, "Available"])

    print("Book added successfully.")


def search_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book[0] == book_id:
            print(book)
            return

    print("Book not found.")


def issue_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return

    print("Book not found.")


def return_book():
    book_id = input("Enter book ID: ")

    for book in books:
        if book[0] == book_id:
            book[3] = "Available"
            print("Book returned successfully.")
            return

    print("Book not found.")


def display_books():
    print("\nAvailable books:")

    for book in books:
        if book[3] == "Available":
            print(book)


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_books()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")