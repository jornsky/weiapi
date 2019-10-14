"""
 Created by 七月 on 2018/5/8.
"""

from app.libs.error_code import Success,  NotFound
from app.libs.redprint import Redprint
from flask import jsonify, current_app

from app.models.base import db
from app.models.subject import Subject

from payjs import PayJS # 也可根据个人习惯选择使用 Payjs/PAYJS/payjs
from payjs import PayJSNotify # 也可根据个人习惯选择使用 PayjsNotify/PAYJSNotify

MCHID = '1542409151'
KEY = '3E1HrQYV6WHOWv5V'


# 初始化
p = PayJS(MCHID, KEY)

# 扫码支付
OUT_TRADE_NO = '2017TEST' # 外部订单号（自己的支付系统的订单号，请保证唯一）
TOTAL_FEE = 1 # 支付金额，单位为分，金额最低 0.01 元最多 10000 元
BODY = '测试支付' # 订单标题
NOTIFY_URL = 'https://pay.singee.site/empty/' # Notify 网址
ATTACH = 'info' # Notify 内容

__author__ = '七月'

api = Redprint('subject')

@api.route('/add/<string:title>/<string:content>/<string:cate>')
def add_subject(title,content,cate):


    with db.auto_commit():
        sub = Subject()
        sub.title = title
        sub.content = content
        sub.cate = cate
        db.session.add(sub)


    return Success()



#更具title模糊查询
@api.route('/get/<string:title>')
def get_subject(title):

    re = Subject().query.filter(Subject.title.like("%" + title + "%")if title is not None else "").all()


    return jsonify(re)

#更具id查询
@api.route('/get/<int:id>')
def get_subject_byid(id):
    re = Subject.query.get(id)

    if not re:
        return NotFound()


    return jsonify(re)


@api.route('/top')
def get_top():

    return  jsonify (Subject().get_top(current_app.config['VIEW_NUMBER']))



@api.route('/pay')
def pay():
    c = p.get_cashier_url(out_trade_no=OUT_TRADE_NO, total_fee=TOTAL_FEE, body=BODY)

    return  jsonify(c)
