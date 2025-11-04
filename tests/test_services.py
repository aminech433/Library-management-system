# tests/test_services.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.library.services import LibraryService

class TestLibraryService:
    def test_add_book(self):
        service = LibraryService()
        book = service.add_book("Python", "Author", "1234567890", 3)
        
        assert book.title == "Python"
        assert book.isbn == "1234567890"
        assert len(service.books) == 1
    
    def test_find_book_by_isbn(self):
        service = LibraryService()
        service.add_book("Book1", "Author1", "1111111111")
        service.add_book("Book2", "Author2", "2222222222")
        
        found = service.find_book_by_isbn("2222222222")
        assert found.title == "Book2"
        
        not_found = service.find_book_by_isbn("9999999999")
        assert not_found is None
    
    def test_get_available_books(self):
        service = LibraryService()
        book1 = service.add_book("Available", "Author", "1111111111", 2)
        book2 = service.add_book("Unavailable", "Author", "2222222222", 1)
        
        # Rendre le deuxième livre indisponible
        book2.borrow()
        
        available_books = service.get_available_books()
        assert len(available_books) == 1
        assert available_books[0].title == "Available"
    
    def test_add_user(self):
        service = LibraryService()
        user = service.add_user("john", "john@example.com", "LIBRARIAN")
        
        assert user.username == "john"
        assert user.email == "john@example.com"
        assert user.role == "LIBRARIAN"
        assert len(service.users) == 1
    
    def test_find_user_by_id(self):
        service = LibraryService()
        service.add_user("user1", "user1@example.com")
        service.add_user("user2", "user2@example.com")
        
        found = service.find_user_by_id(2)
        assert found.username == "user2"
        
        not_found = service.find_user_by_id(999)
        assert not_found is None