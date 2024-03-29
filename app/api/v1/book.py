"""
 Created by 七月 on 2018/5/8.
"""
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.validators.forms import BookSearchForm
from flask import jsonify

__author__ = '七月'

api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    # book = Book()
    # 元类 ORM
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    books = [book.hide('summary') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)


@api.route('/hehe')
def hehe():
    return  'hehe'
