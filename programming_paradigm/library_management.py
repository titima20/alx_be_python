class Book:
    """A class to represent a book."""

    def __init__(self, title, author):
        self.title = title               # Public attribute
        self.author = author             # Public attribute
        self._is_checked_out = False      # Private attribute

    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    """A class to represent a library."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"You have checked out '{title}'."
                else:
                    return f"The book '{title}' is already checked out."
        return f"The book '{title}' does not exist in the library."

    def return_book(self, title):
        """Return a book to the library."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"You have returned '{title}'."
                else:
                    return f"The book '{title}' was not checked out."
        return f"The book '{title}' does not exist in the library."

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if book.is_available()]
        return available_books if available_books else "No books available."

# Example usage
if __name__ == "__main__":
    # Create library instance
    library = Library()

    # Create some book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List available books
    print("Available books:", library.list_available_books())

    # Check out a book
    print(library.check_out_book("1984"))

    # List available books after checking out one
    print("Available books:", library.list_available_books())

    # Return a book
    print(library.return_book("1984"))

    # List available books after returning
    print("Available books:", library.list_available_books())
