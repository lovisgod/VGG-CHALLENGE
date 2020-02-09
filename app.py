from flask import Flask
from flask import request
from flask import jsonify
from db.database import db_session, init_db
from controllers.register import signup

app = Flask(__name__)

init_db()


@app.route('/')
def home():
    return "Hello VGG"

@app.route('/api/users/register', methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    response = signup(db_session, name, password)
    return jsonify(
        status = "success",
        message = response
    )


# close db when the app is down. this handle the lifecycle of the db to avoid memory leakage
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()    
    

if __name__ =="__main__":
    app.run(debug=True,port=8080)