from app import db
from datetime import datetime


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True)
    author = db.Column(db.String(200))
    status = db.Column(db.String(200))

    def __str__(self):
        return f"<id:{self.id}, {self.title} - {self.author_id}, {self.status}>"

book = Book()

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    surname = db.Column(db.String(200))


    def __str__(self):
        return f"<Author {self.id}, {self.name}>"

author = Author()