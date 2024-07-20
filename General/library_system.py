class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book added: {new_book}")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"Sorry, the book '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned '{book.title}'.")
                    return
                else:
                    print(f"The book '{book.title}' was not borrowed.")
                    return
        print(f"The book '{title}' does not belong to this library.")


if __name__ == "__main__":
    my_library = Library()

    # Adding books to the library
    my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    my_library.add_book("To Kill a Mockingbird", "Har
