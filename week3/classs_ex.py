class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False


class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError(f"Expected a Book instance, got {type(book).__name__}")
            self.books = list(books)

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"Expected a Book instance, got {type(book).__name__}")
        self.books.append(book)

    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = True
                print(f"'{book_name}' marked as read.")
                return
        print(f"'{book_name}' is not in the collection.")

    def list_books(self):
        if not self.books:
            print("The collection is empty.")
            return
        for book in self.books:
            status = "Read" if book.read else "Not read"
            print(f"{book.name} by {book.author} ({book.release_date}) - {status}")


if __name__ == "__main__":
    b1 = Book("1984", "George Orwell", 1949)
    b2 = Book("Brave New World", "Aldous Huxley", 1932)
    b3 = Book("Fahrenheit 451", "Ray Bradbury", 1953)

    collection = BookCollection([b1, b2])
    collection.add_book(b3)

    print("All books:")
    collection.list_books()

    print()
    collection.mark_as_read("1984")

    print("\nAfter marking '1984' as read:")
    collection.list_books()

    print()
    collection.mark_as_read("The Catcher in the Rye")