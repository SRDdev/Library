"""
Module to manage user operations.
"""
from src.models import User
from src import storage

class UserManager:
    """
    Class to manage users.
    """

    def __init__(self):
        """
        Initialize UserManager and load users from storage.
        """
        self.users = storage.load_users()

    def add_user(self, name, user_id):
        """
        Add a new user.
        """
        if self.find_user(user_id=user_id) is not None:
            print("User with the same UserID already exists. Please choose a different UserID.")
            return
        user = User(name, user_id)
        self.users.append(user)
        storage.save_users(self.users)
        print("User added successfully.")

    def list_users(self):
        """
        List all users.
        """
        for user in self.users:
            print(user)

    def find_user(self, **kwargs):
        """
        Find a user by given criteria.
        """
        for user in self.users:
            if all(getattr(user, k) == v for k, v in kwargs.items()):
                return user
        return None
