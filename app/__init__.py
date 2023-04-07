import os

from flasgger import Swagger
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'user')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'database')

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DATABASE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    swagger = Swagger(app)

    with app.app_context():
        db.create_all()

    return app
