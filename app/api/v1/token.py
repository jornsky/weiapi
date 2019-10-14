"""
 Created by 七月 on 2018/5/13.
"""
from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm, TokenForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, \
    BadSignature

api = Redprint('token')

__author__ = '七月'

#拿到token就是登入了
@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # 生成Token 1、加密 2、加入用户的信息
    expiration = current_app.config['TOKEN_EXPIRATION']

    #生成令牌
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)

    #生成token  这里序列化器生成的是byte类型
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


@api.route('/secret', methods=['POST'])
def get_token_info():
    """获取令牌信息"""
    form = TokenForm().validate_for_api()
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data, return_header=True)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)

    r = {
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    }
    return jsonify(r)


# """生成令牌"""
# """生成令牌"""
# """生成令牌"""
# """生成令牌"""
def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """生成令牌"""
    #序列化期
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)

    #写入信息
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope':scope
    })
