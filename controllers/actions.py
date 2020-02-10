from db.models import Action, Project
import json
from flask_jwt_extended import create_access_token, jwt_required

@jwt_required
def addAction(db_session, project_id, description, note):
    try:
        project = db_session.query(Project).filter(Project.id == project_id).first()
        if project is None:
            errorResp = {'status': 'Error', 'message': 'project not found'}
            return errorResp
        action = Action(project_id=project_id, description=description, note=note)
        db_session.add(action)
        db_session.commit()
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    res = {'status': 'Success', 'message': 'Action successfully added'}
    return res


@jwt_required
def getAllActions(db_session):
    try:
        actions = []
        for row in db_session.query(Action).all():
            actions.append({'id': row.id, 'project_id': row.project_id, 'description': row.description, 'note': row.note})
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if actions is None:
        errorResp = {'status': 'Error', 'message': 'actions not found'}
        return errorResp
    res = {'status': 'Success', 'data': actions}
    return res


@jwt_required
def getActionsForAProject(db_session, id):
    try:
        project = db_session.query(Project).filter(Project.id == id).first()
        if project is None:
            errorResp = {'status': 'Error', 'message': 'project not found'}
            return errorResp
        actions = []
        for row in db_session.query(Action).filter(Action.project_id == id).all():
            actions.append({'id': row.id, 'project_id': row.project_id, 'description': row.description, 'note': row.note})
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if actions is None:
        errorResp = {'status': 'Error', 'message': 'actions not found'}
        return errorResp
    res = {'status': 'Success', 'data': actions}
    return res


@jwt_required
def getAnActionById(db_session, id):
    try:
        action = db_session.query(Action).filter(Action.id == id).first()
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if action is None:
        errorResp = {'status': 'Error', 'message': 'action not found'}
        return errorResp
    res = {'status': 'Success', 'data': action.__repr__()}
    return res


@jwt_required
def getAnActionByActionAndProjectId(db_session, project_id, action_id):
    try:
        project = db_session.query(Project).filter(Project.id == project_id).first()
        if project is None:
            errorResp = {'status': 'Error', 'message': 'project not found'}
            return errorResp
        action = db_session.query(Action).filter(Action.id == action_id, project_id == project_id).first()
        if project is None:
            errorRes = {'status': 'Error', 'message': 'action not found'}
            return errorRes
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if action is None:
        errorResp = {'status': 'Error', 'message': 'action not found'}
        return errorResp
    res = {'status': 'Success', 'data': action.__repr__()}
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
