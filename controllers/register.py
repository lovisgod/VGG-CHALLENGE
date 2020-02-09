from db.models import User

def signup(db_session, name, password):
    try:
         user = User(name=name, password= password)
         db_session.add(user)
         db_session.commit()
    except Exception as e:
        # return "Registration not successful please login with your details please check your password and name and try again"
        
    return "Registration successful please login with your details"