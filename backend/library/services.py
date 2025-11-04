# backend/library/services.py
from .models import Book, User

class LibraryService:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, title, author, isbn, copies=1):
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        return book
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def get_available_books(self):
        return [book for book in self.books if book.is_available()]
    
    def add_user(self, username, email, role="MEMBER"):
        user_id = len(self.users) + 1
        user = User(user_id, username, email, role)
        self.users.append(user)
        return user
    
    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None