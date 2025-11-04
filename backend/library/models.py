# backend/library/models.py

class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def is_available(self):
        return self.available_copies > 0
    
    def borrow(self):
        if self.is_available():
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def __str__(self):
        return f"{self.title} by {self.author}"

class User:
    def __init__(self, user_id, username, email, role="MEMBER"):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role
        self.is_active = True
    
    def can_borrow(self):
        return self.is_active and self.role in ["MEMBER", "LIBRARIAN"]
    
    def get_role_display(self):
        roles = {
            "MEMBER": "Membre",
            "LIBRARIAN": "Bibliothécaire", 
            "ADMIN": "Administrateur"
        }
        return roles.get(self.role, self.role)