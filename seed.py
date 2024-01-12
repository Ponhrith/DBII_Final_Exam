from models import *
def seed_books():
    books_data = [
        {
            'isbn': '1234567890123',
            'title': 'Sample Book 1',
            'author': 'Author 1',
            'genre': 'Fiction',
            'price': 19.99,
            'quantity_available': 100
        },
        {
            'isbn': '9876543210987',
            'title': 'Sample Book 2',
            'author': 'Author 2',
            'genre': 'Non-Fiction',
            'price': 29.99,
            'quantity_available': 50
        },
    ]
    for book_data in books_data:
        book = Book(**book_data)
        db.session.add(book)
    db.session.commit()