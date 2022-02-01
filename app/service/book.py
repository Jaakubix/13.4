from app import db, models

class DbBook():
    def __init__(self, model):
        self.model = model

    def get_books(self):
        data = self.model.query.all()
        data = [d.to_dict() for d in data]
        return data

    def get_book(self, id):
        data = self.model.query.filter_by(id=id).first()
        return data.to_dict()

    def add_book(self, author, title, status):
        book = self.model(author=author, title=title, status=status)
        db.session.add(book)
        db.session.commit()

    def book_update(self, id, author, title, status):
        data = self.model.query.filter_by(id=id).first()
        book = self.model(author=author, title=title, status=status)
        db.session.delete(data)
        db.session.add(book)
        db.session.commit()

db_book = DbBook(model=models.Book)