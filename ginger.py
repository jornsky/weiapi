"""
 Created by 七月 on 2018/5/7.
"""
from werkzeug.exceptions import HTTPException
from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = '七月'

app = create_app()



#捕捉一切错误
@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5002)
