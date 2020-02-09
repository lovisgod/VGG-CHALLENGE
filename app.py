from flask import Flask
from flask import request
from flask import jsonify, Response
import json
from flask_jwt_extended import JWTManager
from db.database import db_session, init_db
from controllers.register import signup
from controllers.auth import sign_in
from controllers.projects import addProjects, getAllProjects

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'

init_db()
jwt = JWTManager(app)


@app.route('/')
def home():
    return "Hello VGG"

@app.route('/api/users/register', methods=["POST"])
def register():
    name = request.form.get("name")
    password = request.form.get("password")
    response = signup(db_session, name, password)
    return jsonify(response)

@app.route('/api/users/auth', methods=["POST"])
def auth():
    name = request.form.get("name")
    password = request.form.get("password")
    response = sign_in(db_session, name, password)
    return response

@app.route('/api/projects', methods=["POST"])
def createProject():
    name = request.form.get("name")
    description = request.form.get("description")
    completed = False
    response = addProjects(db_session, name, description, completed)
    return jsonify(response)
@app.route('/api/projects', methods=["GET"])
def listAllProjects():
    return jsonify(getAllProjects(db_session))


# close db when the app is down. this handle the lifecycle of the db to avoid memory leakage
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()    
    

if __name__ =="__main__":
    app.run(debug=True,port=8080)