from db.models import User
import json

def signup(db_session, name, password):
    try:
         user = User(name=name, password= password)
         db_session.add(user)
         db_session.commit()
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    res = {'status': 'Success', 'message': 'Registration successful please login with your details'}
    return res