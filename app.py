from flask import Flask
from flask import request
from flask import jsonify, Response
from flask_request_params import bind_request_params
import json
from flask_jwt_extended import JWTManager
from db.database_util import db_session, init_db
from controllers.register import signup
from controllers.auth import sign_in
from controllers.projects import addProjects, getAllProjects, getAProjectById, updateAProjectByID, updateAProjectCompleted, deleteAJobByID
from controllers.actions import addAction, getAllActions, getActionsForAProject, getAnActionById, getAnActionByActionAndProjectId

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.before_request(bind_request_params)

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


@app.route('/api/projects/<project_id>', methods=["GET"])
def findAProjectById(project_id):
    return getAProjectById(db_session, project_id)


@app.route('/api/projects', methods=["GET"])
def listAllProjects():
    return jsonify(getAllProjects(db_session))


@app.route('/api/projects/<project_id>', methods=['PUT'])
def updateProjectById(project_id):
    name = request.form.get('name')
    description = request.form.get('description')
    return jsonify(updateAProjectByID(db_session, project_id, name, description))


@app.route('/api/projects/<project_id>', methods=['PATCH'])
def updateProjectCompletion(project_id):
    return jsonify(updateAProjectCompleted(db_session, project_id))


@app.route('/api/projects/<project_id>', methods=['DELETE'])
def deleteAProject(project_id):
    return jsonify(deleteAJobByID(db_session, project_id))


@app.route('/api/projects/<projectId>/actions', methods=['POST'])
def addActionToProject(projectId):
    description = request.form.get('description')
    note = request.form.get('note')
    return jsonify(addAction(db_session, projectId, description, note))


@app.route('/api/actions', methods=['GET'])
def listAllActions():
    return jsonify(getAllActions(db_session))


@app.route('/api/projects/<projectId>/actions', methods=['GET'])
def listProjectActions(projectId):
    return jsonify(getActionsForAProject(db_session, projectId))


@app.route('/api/actions/<actionId>', methods=['GET'])
def getAnAction(actionId):
    return jsonify(getAnActionById(db_session, actionId))


@app.route('/api/projects/<projectId>/actions/<actionId>', methods=['GET'])
def getAnActionByProjectAndId(projectId, actionId):
    return jsonify(getAnActionByActionAndProjectId(db_session, projectId, actionId))

# close db when the app is down. this handle the lifecycle of the db to avoid memory leakage
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == "__main__":
    app.run(debug=True)
