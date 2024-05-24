"""
Module to handle storage operations for books, users, and checkouts.
"""
import json
from src.models import Book, User, Checkout

BOOKS_FILE = 'data/books.json'
USERS_FILE = 'data/users.json'
CHECKOUTS_FILE = 'data/checkouts.json'

def load_books():
    """
    Load books from the JSON file.
    """
    try:
        with open(BOOKS_FILE, 'r' ,encoding='utf8') as file:
            books_data = json.load(file)
            return [Book(**data) for data in books_data]
    except FileNotFoundError:
        return []

def save_books(books):
    """
    Save books to the JSON file.
    """
    with open(BOOKS_FILE, 'w',encoding='utf8') as file:
        json.dump([book.__dict__ for book in books], file)

def load_users():
    """
    Load users from the JSON file.
    """
    try:
        with open(USERS_FILE, 'r',encoding='utf8') as file:
            users_data = json.load(file)
            return [User(**data) for data in users_data]
    except FileNotFoundError:
        return []

def save_users(users):
    """
    Save users to the JSON file.
    """
    with open(USERS_FILE, 'w',encoding='utf8') as file:
        json.dump([user.__dict__ for user in users], file)

def load_checkouts():
    """
    Load checkouts from the JSON file.
    """
    try:
        with open(CHECKOUTS_FILE, 'r',encoding='utf8') as file:
            checkouts_data = json.load(file)
            return [Checkout(**data) for data in checkouts_data]
    except FileNotFoundError:
        return []

def save_checkouts(checkouts):
    """
    Save checkouts to the JSON file.
    """
    with open(CHECKOUTS_FILE, 'w',encoding='utf8') as file:
        json.dump([checkout.__dict__ for checkout in checkouts], file)
