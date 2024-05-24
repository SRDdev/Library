"""
Module to manage checkouts.
"""
from src.models import Checkout
from src import storage
from src.book import BookManager

class CheckoutManager:
    """
    Class to manage checkouts.
    """

    def __init__(self):
        """
        Initialize CheckoutManager and load checkouts from storage.
        """
        self.reload_checkouts()

    def reload_checkouts(self):
        """
        Reload checkouts from storage.
        """
        self.checkouts = storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        """
        Checkout a book.
        """
        book_manager = BookManager()
        book = book_manager.find_book(isbn=isbn)
        if book is None:
            print("Book not found.")
            return

        if not book.available:
            print("Book is not available for checkout.")
            return

        self.reload_checkouts()
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        storage.save_checkouts(self.checkouts)
        book.available = False
        book_manager.update_book(book)
        print("Book checked out successfully.")

    def return_book(self, user_id, isbn):
        """
        Return a book.
        """
        book_manager = BookManager()
        book = book_manager.find_book(isbn=isbn)
        if book is None:
            print("Book not found.")
            return

        self.reload_checkouts()
        checkout = self.find_checkout(user_id=user_id, isbn=isbn)
        if checkout is None:
            print("No checkout record found for this user and book.")
            return

        self.checkouts.remove(checkout)
        storage.save_checkouts(self.checkouts)
        book.available = True
        book_manager.update_book(book)
        print("Book returned successfully.")

    def list_checkouts(self):
        """
        List all checkouts.
        """
        self.reload_checkouts()
        for checkout in self.checkouts:
            print(checkout)

    def find_checkout(self, **kwargs):
        """
        Find a checkout by given criteria.
        """
        self.reload_checkouts()
        for checkout in self.checkouts:
            if all(getattr(checkout, k) == v for k, v in kwargs.items()):
                return checkout
        return None
