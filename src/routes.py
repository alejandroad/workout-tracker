from flask import Blueprint, Response, request  # import request here

user_routes = Blueprint('user_routes', __name__)

from .models import User, db

def init_app(app):

    @app.route('/')
    def index():
        return "Hello World"

    # User routes
    @app.route('/users', methods=['POST'])
    def add_user():
        app.logger.info("Inside add_user()")
        data = request.json
        app.logger.info(f"Received request: {str(data)}")

        name = data['name']
        username = data['username']
        password = data['password_hash']

        already_registered = db.session.query(User).filter_by(name=name).first()
        if already_registered:
            return Response(f"User {username} already exists", status=400)

        user = User(name=name, username=username)
        user.set_password(password)  # Corrected from password_hash

        db.session.add(user)
        db.session.commit()

        return Response(f"User {username} successfully added", status=200)

    @app.route('/users', methods=['GET'])
    def get_users():
        app.logger.info("Inside get_users()")
        users = db.session.query(User)
        user_list = [user.as_dict() for user in users]  # Corrected this line
        return {"users": user_list}, 200

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):  # Changed id to user_id
        app.logger.info(f"Inside get_user() with id {user_id}")
        user = db.session.query(User).get(user_id)  # Corrected this line
        if user is None:
            return Response(f"User with id {user_id} not found", status=404)
        app.logger.info(f"Found user {str(user)}")
        return user.as_dict(), 200

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):  # Changed id to user_id
        app.logger.info("Inside delete_user()")
        user = db.session.query(User).get(user_id)  # Corrected this line
        if user is None:
            return Response(f"User with id: {user_id} does not exist", status=404)
        app.logger.info(f"Found user with id: {user_id}")
        app.logger.info("Deleting user...")
        db.session.delete(user)  # Corrected this line
        db.session.commit()
        return Response(f"User with id: {user_id} has been deleted", status=200)
