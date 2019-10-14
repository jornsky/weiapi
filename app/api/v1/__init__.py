"""
 Created by 七月 on 2018/5/8.
"""
from flask import Blueprint
from app.api.v1 import  book, client, token,queti,subject,askanswer,problem

__author__ = '七月'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    queti.api.register(bp_v1)
    subject.api.register(bp_v1)
    askanswer.api.register(bp_v1)
    problem.api.register(bp_v1)
    return bp_v1
