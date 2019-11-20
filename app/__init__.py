from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS, cross_origin
from flask_jsonpify import jsonify

app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

from app.models import tables
from app.controller import user_ws
from app.controller import turma_ws
