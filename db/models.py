from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from database import metadata, db_session

class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Project(object):
    query = db_session.query_property()

    def __init__(self, name=None, description=None, completed=None):
        self.name = name
        self.description = description
        self.completed = completed

    def __repr__(self):
        return '<Project %r>' % (self.name)

class Action(object):
    query = db_session.query_property()

    def __init__(self, project_id=None, description=None, note=None):
        self.project_id = project_id
        self.description = description
        self.note = note

    def __repr__(self):
        return '<Action %r>' % (self.project_id)

projects = Table('projects', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('description', String(120)),
    Column('completed', Boolean, default= False, nullable= False)
)
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('password', String(120), unique=True)
)

actions = Table('actions', metadata,
    Column('id', Integer, primary_key=True),
    Column('project_id', Integer),
    Column('description', String(120)),
    Column('note',  String(500))
)
mapper(User, users)
mapper(Project, projects)
mapper(Action, actions)