from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src import routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///powerlifting.db'

    db.init_app(app)

    return app