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
        if action is None:
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
def updateAnActionByID(db_session, projectId, actionId, description, note):
    try:
        project = db_session.query(Project).filter(Project.id == projectId).first()
        if project is None:
            errorResp = {'status': 'Error', 'message': 'project not found'}
            return errorResp
        action = db_session.query(Action).filter(Action.id == actionId, projectId == projectId).first()
        if action is None:
            errorRes = {'status': 'Error', 'message': 'action not found'}
            return errorRes
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    if note is not None:
        action.note = note
    if description is not None:
        action.description = description
    db_session.commit()
    res = {'status': 'Success', 'data': 'Project action successfully updated'}
    return res


@jwt_required
def deleteAnActionByID(db_session, projectId, actionId):
    try:
        project = db_session.query(Project).filter(Project.id == projectId).first()
        if project is None:
            errorResp = {'status': 'Error', 'message': 'project not found'}
            return errorResp
        action = db_session.query(Action).filter(Action.id == actionId, projectId == projectId).first()
        if action is None:
            errorRes = {'status': 'Error', 'message': 'action not found'}
            return errorRes
    except BaseException as e:
        errorRes = {'status': 'Error', 'message': e.message}
        return errorRes
    db_session.delete(action)
    db_session.commit()
    res = {'status': 'Success', 'data': 'Action successfully deleted'}
    return res
