from flask import current_app

def init_app(app):
    @app.route('/')
    def index():
        return "Hello World"
