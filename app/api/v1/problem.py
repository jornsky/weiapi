"""
 Created by 七月 on 2018/5/8.
"""

from app.libs.error_code import Success
from app.libs.redprint import Redprint

from app.models.problem import Problem
from app.models.base import db

__author__ = '七月'

api = Redprint('problem')

@api.route('/add/<string:ques>')
def add_pro(ques):


    with db.auto_commit():
        pro = Problem()
        pro.ques = ques
        db.session.add(pro)


    return Success()





