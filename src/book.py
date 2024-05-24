"""
Module to manage books.
"""
from tabulate import tabulate
from src import storage
from src.models import Book

class BookManager:
    """
    Class to manage books.
    """
    def __init__(self):
        """
        Initialize BookManager and load books from storage.
        """
        self.reload_books()

    def reload_books(self):
        """
        Reload books from storage.
        """
        self.books = storage.load_books()

    def add_book(self, title, author, isbn):
        """
        Add a new book to the collection.
        """
        self.reload_books()
        if self.find_book(isbn=isbn) is not None:
            print("A book with the same ISBN already exists. Please choose a different ISBN.")
            return
        book = Book(title, author, isbn)
        self.books.append(book)
        storage.save_books(self.books)
        print("Book added successfully.")

    def update_book(self, updated_book):
        """
        Update an existing book in the collection.
        """
        self.reload_books()
        for i, book in enumerate(self.books):
            if book.isbn == updated_book.isbn:
                self.books[i] = updated_book
                storage.save_books(self.books)
                return
        print("Book not found.")

    def list_books(self):
        """
        List all available books.
        """
        self.reload_books()
        book_list = [
            [book.title, book.author, book.isbn]
            for book in self.books if book.available
        ]
        headers = ["Title", "Author", "ISBN"]
        print(tabulate(book_list, headers, tablefmt="grid"))

    def find_book(self, **kwargs):
        """
        Find a book by given criteria.
        """
        self.reload_books()
        for book in self.books:
            if all(getattr(book, k) == v for k, v in kwargs.items()):
                return book
        return None
    