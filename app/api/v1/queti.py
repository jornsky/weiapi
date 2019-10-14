"""
 Created by 七月 on 2018/5/8.
"""
from sqlalchemy import or_

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from flask import jsonify, request

from app.models.questi import Questi
from app.models.base import db

__author__ = '七月'

api = Redprint('quti')

@api.route('/add/<string:qu>/<string:an>')
def add_ti(qu,an):


    with db.auto_commit():
        quti = Questi()
        quti.question = qu
        quti.answer = an
        db.session.add(quti)


    return Success()



#题库查询
@api.route('/get/<string:qu>')
def search_ti(qu):

    re = Questi().query.filter(Questi.question.like("%" + qu + "%")if qu is not None else "").first_or_404()


    return jsonify(re)


