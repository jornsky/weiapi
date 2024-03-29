"""
 Created by 七月 on 2018/5/7.
"""
from .app import Flask
from werobot import WeRoBot
from werobot.contrib.flask import make_view


myrobot = WeRoBot(token='weixin')

__author__ = '七月'


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.add_url_rule(rule='/robot/',  # WeRoBot 挂载地址
                     endpoint='werobot',  # Flask 的 endpoint
                     view_func=make_view(myrobot),
                     methods=['GET', 'POST'])
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprints(app)
    register_plugin(app)

    return app

