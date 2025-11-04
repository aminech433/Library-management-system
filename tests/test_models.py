# tests/test_models.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.library.models import Book, User

class TestBook:
    def test_book_creation(self):
        book = Book("Python Guide", "John Doe", "1234567890", 5)
        assert book.title == "Python Guide"
        assert book.author == "John Doe"
        assert book.isbn == "1234567890"
        assert book.total_copies == 5
        assert book.available_copies == 5
    
    def test_book_availability(self):
        book = Book("Test Book", "Author", "1111111111", 3)
        assert book.is_available() == True
        
        # Emprunter tous les livres
        book.borrow()
        book.borrow()
        book.borrow()
        assert book.is_available() == False
    
    def test_book_borrow_return(self):
        book = Book("Demo Book", "Writer", "9999999999", 2)
        assert book.borrow() == True
        assert book.available_copies == 1
        assert book.return_book() == True
        assert book.available_copies == 2
    
    def test_book_string_representation(self):
        book = Book("Django", "Author", "1234567890")
        assert str(book) == "Django by Author"

class TestUser:
    def test_user_creation(self):
        user = User(1, "john_doe", "john@example.com", "MEMBER")
        assert user.user_id == 1
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.role == "MEMBER"
        assert user.is_active == True
    
    def test_user_can_borrow(self):
        active_user = User(1, "user1", "user1@example.com", "MEMBER")
        inactive_user = User(2, "user2", "user2@example.com", "MEMBER")
        inactive_user.is_active = False
        
        assert active_user.can_borrow() == True
        assert inactive_user.can_borrow() == False
    
    def test_user_role_display(self):
        user = User(1, "admin", "admin@example.com", "ADMIN")
        assert user.get_role_display() == "Administrateur"