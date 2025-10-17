from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Swim@01580420'

    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

    app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'mov', 'avi'}

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'videos.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from . import routes
    app.register_blueprint(routes.main)

    return app