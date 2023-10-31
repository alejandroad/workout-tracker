from flask import Blueprint, Response

user_routes = Blueprint('user_routes', __name__)

from .models import User, Exercise, Workout, db

def init_app(app):

    @app.route('/')
    def index():
        return "Hello World"

    # User routes
    @app.route('/register', methods=['POST'])
    def add_user():
        app.logger("Inside add_user")
        data = request.json
        app.logger("Recieved request: %s", str(data))

        name = data['name']
        username = data['username']
        password = data['password_hash']

        already_registered = db.session.query(User).filter_by(name=name).first()
        if already_registered:
            return Response(f"User {username} already exists", status = 400)

        # a newly registered worker should have no workouts, null ?
        user = User(name=name, username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return Response(f"User {username} successfully added", status =200)

