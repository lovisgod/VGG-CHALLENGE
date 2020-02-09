from db.models import User
import json
from flask_jwt_extended import create_access_token
from datetime import timedelta


def sign_in(db_session, name, password):
    try:
         user = User.query.filter(User.name == name, User.password == password).first()
         print(user)
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if user == None:
        errorResp = {'status': 'Error', 'message': 'user not found'}
        return errorResp
    expires = timedelta(days=1)    
    access_token = create_access_token(identity=str(user), expires_delta= expires)
    res = {'status': 'Success', 'access_token': str(access_token)}
    return res