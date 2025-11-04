# backend/utils/helpers.py

def validate_email(email):
    """Valide un format d'email basique"""
    return "@" in email and "." in email

def validate_isbn(isbn):
    """Valide un format ISBN basique"""
    return isbn and len(isbn) in [10, 13] and isbn.isdigit()

def calculate_due_date(days=14):
    """Calcule une date d'échéance"""
    from datetime import datetime, timedelta
    return datetime.now() + timedelta(days=days)