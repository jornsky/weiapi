"""
 Created by 七月 on 2018/5/10.
"""
from flask import request, jsonify

from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from werkzeug.exceptions import HTTPException

__author__ = '七月'

api = Redprint('client')


#注册加登入
@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data)
