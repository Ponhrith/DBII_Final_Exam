from flask import Flask, request
from flask_restx import Api, Resource, fields, reqparse
from config import Config
from models import db, Book
from seed import seed_books

config = Config()
app = Flask(__name__)
api = Api(app)
api_ns = api.namespace("api", path='/', description="API")
app.config.from_object(config)

db.init_app(app)
with app.app_context():
    db.create_all()
    if Book.query.count() == 0:
        seed_books()

book_model = api.model('Book', {
    'id': fields.Integer,
    'isbn': fields.String,
    'title': fields.String,
    'author': fields.String,
    'genre': fields.String,
    'price': fields.Float,
    'quantity_available': fields.Integer,
})

book_parser = reqparse.RequestParser()
book_parser.add_argument('isbn', required=True)
book_parser.add_argument('title', required=True)
book_parser.add_argument('author', required=True)
book_parser.add_argument('genre', required=True)
book_parser.add_argument('price', required=True, type=float)
book_parser.add_argument('quantity_available', required=True, type=int)

@api_ns.route('/book')
class Books(Resource):
    @api_ns.marshal_with(book_model, as_list=True)
    def get(self):
        return Book.query.all()

    @api_ns.expect(book_model)
    @api_ns.marshal_with(book_model)
    def post(self):
        args = book_parser.parse_args()
        book = Book(**args)
        db.session.add(book)
        db.session.commit()
        return book

@api_ns.route('/book/<int:id>')
class BookById(Resource):
    @api_ns.marshal_with(book_model)
    def get(self, id):
        return Book.query.get_or_404(id)

    @api_ns.expect(book_model)
    @api_ns.marshal_with(book_model)
    def put(self, id):
        book = Book.query.get_or_404(id)
        args = book_parser.parse_args()
        for key, value in args.items():
            setattr(book, key, value)
        db.session.commit()
        return book

    @api_ns.marshal_with(book_model)
    def delete(self, id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return book

@api_ns.route('/book/author/<string:author>')
class BooksByAuthor(Resource):
    @api_ns.marshal_with(book_model, as_list=True)
    def get(self, author):
        return Book.query.filter_by(author=author).all()

@api_ns.route('/book/isbn/<string:isbn>')
class BookByISBN(Resource):
    @api_ns.marshal_with(book_model)
    def get(self, isbn):
        return Book.query.filter_by(isbn=isbn).first()

@api_ns.route('/book/genre/<string:genre>')
class BooksByGenre(Resource):
    @api_ns.marshal_with(book_model, as_list=True)
    def get(self, genre):
        return Book.query.filter_by(genre=genre).all()

if __name__ == '__main__':
    app.run(debug=True)
