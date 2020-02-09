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