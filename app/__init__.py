from flask import Flask
from flask_login import LoginManager
from models import db, User
from routes import auth, index, predict

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use a proper database in a production environment
    db.init_app(app)

    login_manager = LoginManager(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(index)
    app.register_blueprint(auth)
    app.register_blueprint(predict)

    return app
