"""
Module defining book-related classes.
"""
class Book:
    """
    Represents a book.
    """
    def __init__(self, title, author, isbn, available=True):
        """
        Initialize a Book instance.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        """
        Return a string representation of the Book instance.
        """
        return f"Book(title={self.title}, author={self.author}, isbn={self.isbn}, available={self.available})"


class User:
    """
    Represents a user.
    """
    def __init__(self, name, user_id):
        """
        Initialize a User instance.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """
        Return a string representation of the User instance.
        """
        return f"User(name={self.name}, user_id={self.user_id})"


class Checkout:
    """
    Represents a book checkout by a user.
    """
    def __init__(self, user_id, isbn):
        """
        Initialize a Checkout instance.
        """
        self.user_id = user_id
        self.isbn = isbn

    def __str__(self):
        """
        Return a string representation of the Checkout instance.
        """
        return f"Checkout(user_id={self.user_id}, isbn={self.isbn})"
