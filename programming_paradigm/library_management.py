# library_management.py

class Book:
    """A class representing a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and checkout status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class representing a library that stores books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")
    
    def return_book(self, title):
        """Return a book by title, making it available again."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")
    
    def list_available_books(self):
        """List all available books that are not checked out."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
# main.py

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
