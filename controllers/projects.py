from db.models import Project
import json
from flask_jwt_extended import create_access_token, jwt_required

@jwt_required
def addProjects(db_session, name, description, completed):
    try:
         project = Project(name=name, description= description, completed= completed)
         db_session.add(project)
         db_session.commit()
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    res = {'status': 'Success', 'message': 'Project successfully added'}
    return res

@jwt_required
def getAllProjects(db_session):
    try:
         projects = []
         for row in db_session.query(Project).all():
            projects.append({'id': row.id, 'name': row.name, 'description': row.description, 'completed': row.completed})
    except BaseException as e:
         errorRes = {'status': 'Error', 'message': e.message}
         return errorRes
    if projects == None:
        errorResp = {'status': 'Error', 'message': 'projects not found'}
        return errorResp
    res = {'status': 'Success', 'data': projects}
    return res

@jwt_required
def getAProjectById(db_session, id):
    try:
        project = db_session.query(Project).filter(Project.id == id).first()
    except BaseException as e:
         errorRes = {'status': 'Error', 'message': e.message}
         return errorRes
    if project == None:
        errorResp = {'status': 'Error', 'message': 'project not found'}
        return errorResp
    res = {'status': 'Success', 'data': project.__repr__()}
    return res

@jwt_required
def updateAProjectByID(db_session, id, name, description):
    try:
        project = db_session.query(Project).filter(Project.id == id).first()
    except BaseException as e:
         errorRes = {'status': 'Error', 'message': e.message}
         return errorRes
    if project == None:
        errorResp = {'status': 'Error', 'message': 'project not found'}
        return errorResp
    if name != None:
        project.name = name
    if description != None:
        project.description = description
    db_session.commit()
    res = {'status': 'Success', 'data': 'Project successfully updated'}
    return res

@jwt_required
def updateAProjectCompleted(db_session, id):
    try:
        project = db_session.query(Project).filter(Project.id == id).first()
    except BaseException as e:
         errorRes = {'status': 'Error', 'message': e.message}
         return errorRes
    if project == None:
        errorResp = {'status': 'Error', 'message': 'project not found'}
        return errorResp
    project.completed = True
    db_session.commit()
    res = {'status': 'Success', 'data': 'Project successfully completed'}
    return res

@jwt_required
def deleteAJobByID(db_session, id):
    try:
        project = db_session.query(Project).filter(Project.id == id).first()
    except BaseException as e:
         errorRes = {'status': 'Error', 'message': e.message}
         return errorRes
    if project == None:
        errorResp = {'status': 'Error', 'message': 'project not found'}
        return errorResp
    db_session.delete(project)
    db_session.commit()
    res = {'status': 'Success', 'data': 'Project successfully deleted'}
    return res
