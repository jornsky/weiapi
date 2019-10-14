"""
 Created by 七月 on 2018/5/8.
"""

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.askanswer import Askanswer

from app.models.base import db

__author__ = '七月'

api = Redprint('askanswer')

@api.route('/add/<string:mail>/<string:subject>/<string:cate>')
def add_ask(mail,subject,cate):


    with db.auto_commit():
        ask = Askanswer()
        ask.mail = mail
        ask.subject = subject
        ask.cate = cate

        db.session.add(ask)


    return Success()





