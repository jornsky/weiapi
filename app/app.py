"""
 Created by 七月 on 2018/5/7.
"""
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError
from datetime import date

__author__ = '七月'


class JSONEncoder(_JSONEncoder):
    #jsonfiy()方法默认会调用这里的default  如果遇到无法json的类 falsk会自动调用这里
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            #当一个对象有keys和__gettiem__方法 它的属性可以被 obj['名字'] 这样调用
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder



