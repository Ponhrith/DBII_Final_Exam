from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}', author='{self.author}', genre='{self.genre}', price={self.price}, quantity_available={self.quantity_available})"
    
    
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    biography = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', birthdate={self.birthdate}, biography='{self.biography}')"

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    shipping_address = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}', email='{self.email}', shipping_address='{self.shipping_address}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    shipping_details = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f"Order(id={self.id}, order_date={self.order_date}, total_amount={self.total_amount}, shipping_details='{self.shipping_details}', customer_id={self.customer_id})"
