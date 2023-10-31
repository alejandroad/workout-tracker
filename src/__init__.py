from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import user_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///powerlifting.db'
    app.register_blueprint(user_routes)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app