from flask import Flask, jsonify, abort, make_response, request
from flask.wrappers import Request
from models import book, author
from service.book import db_book
from service.author import db_author
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "ni"

@app.route("/api/v1/lib/", methods=["GET"])
def lib_list_api_v1():
    return jsonify(db_book.get_books())

@app.route("/api/v1/lib/", methods=["POST"])
def add_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'title': request.json[0]['title'],
        'author': request.json[0]['author'],
        'status': request.json[0]['status']
    }
    db_book.post_book(author=book['title'], title=book['title'], status=book['status'])
    return json.dumps({'book': book})

@app.route("/api/v1/lib/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = db_book.get_book(book_id)
    if not book:
        abort(404)
    return json.dumps({'book': book})

@app.route("/api/v1/lib/<int:book_id>", methods=["PUT"])
def book_update(book_id):
    book = db_book.get_book(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('author'), str),
        'done' in data and not isinstance(data.get('status'), bool)
    ]):
        abort(400)
    book = {
        'title': data[0].get('title', book['title']),
        'description': data[0].get('description', book['author']),
        'done': data[0].get('done', book['done'])
    }
    db_book.book_update(id, author=book['author'], title=book['title'], status=book['status'])
    return jsonify({'book': book})

@app.route("/api/v1/bibl/", methods=["GET"])
def bibl_list_api_v1():
    return json.dumps(db_author.get_authors())

@app.route("/api/v1/bibl/", methods=["POST"])
def post_author():
    if not request.json or not all('name' in row for row in request.json):
        abort(400)
    auth = {
        'name': request.json[0]['name'],
        'books': request.json[0]['books']
    }
    db_author.post_author(name=auth['name'], books=auth['books'])
    return jsonify({'author': auth})

@app.route("/api/v1/bibl/<int:id>", methods=["GET"])
def get_author(id):
    auth = db_author.get_author(id)
    if not auth:
        abort(404)
    return jsonify({'author': auth})

@app.route("/api/v1/bibl/<int:id>", methods=["PUT"])
def author_update(id):
    auth = db_author.get_author(id)
    if not auth:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'name' in data and not isinstance(data.get('name'), str),
        'books' in data and not isinstance(data.get('books'), str)
    ]):
        abort(400)
    auth = {
        'name': data[0].get('name', auth['name']),
        'books': data[0].get('books', auth['books'])
    }
    db_author.author_update(id, name=auth['name'], books=auth['books'])
    return jsonify({'author': auth})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)

if __name__ == "__main__":
    app.run(debug=True)