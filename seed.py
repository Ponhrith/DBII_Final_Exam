from models import *
def seed_books():
    books_data = [
        {
            'isbn': '2024001',
            'title': 'The Little Prince',
            'author': 'Antoine de Saint-Exupéry',
            'genre': 'Novel',
            'price': 15,
            'quantity_available': 1000
        },
        {
            'isbn': '2024002',
            'title': 'Animal Farm',
            'author': 'George Orwell',
            'genre': 'Fable',
            'price': 30,
            'quantity_available': 100
        },
    ]
    for book_data in books_data:
        book = Book(**book_data)
        db.session.add(book)
    db.session.commit()