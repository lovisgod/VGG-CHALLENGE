from sqlalchemy import Table, Column, Integer, String, Boolean
from sqlalchemy.orm import mapper
from db.database_util import metadata, db_session


class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password

    def __repr__(self):
        return self.name


class Project(object):
    query = db_session.query_property()

    def __init__(self, name=None, description=None, completed=None):
        self.name = name
        self.description = description
        self.completed = completed

#   this is what is returned when a query is performed on the table
    def __repr__(self):
        return {'name': self.name, 'description': self.description, 'completed': self.completed}


class Action(object):
    query = db_session.query_property()

    def __init__(self, project_id=None, description=None, note=None):
        self.project_id = project_id
        self.description = description
        self.note = note

    def __repr__(self):
        return {'name': self.project_id, 'description': self.description, 'note': self.note}


projects = Table('projects', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('description', String(120)),
    Column('completed', Boolean, default=False, nullable=False)
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
