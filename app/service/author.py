from app import db, models

class DbAuthor():
    def __init__(self, model):
        self.model = model
    
    def get_authors(self):
        data = self.model.query.all()
        data = [d.to_dict() for d in data]
        return data

    def get_author(self, id):
        data = self.model.query.filter_by(id=id).first()
        return data.to_dict()

    def post_author(self, name, books):
        auth = self.model(name=name, books=books)
        db.session.add(auth)
        db.session.commit()

    def author_update(self, id, name, books):
        data = self.model.query.filter_by(id=id).first()
        auth = self.model(name=name, books=books)
        db.session.delete(data)
        db.session.add(auth)
        db.session.commit()

db_author = DbAuthor(model=models.Author)