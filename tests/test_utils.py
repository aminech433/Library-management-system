# tests/test_utils.py
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.utils.helpers import validate_email, validate_isbn

class TestHelpers:
    def test_validate_email(self):
        assert validate_email("test@example.com") == True
        assert validate_email("invalid-email") == False
        assert validate_email("user@domain.co.uk") == True
    
    def test_validate_isbn(self):
        assert validate_isbn("1234567890") == True      # ISBN-10
        assert validate_isbn("1234567890123") == True   # ISBN-13
        assert validate_isbn("123") == False            # Trop court
        assert validate_isbn("invalid") == False        # Pas numérique
        assert validate_isbn("") == False               # Vide