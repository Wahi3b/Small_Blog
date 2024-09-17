
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' #when trying to access a page that requires login in, this will redirect you to the login page
login_manager.login_message_category='info' #makes flash message looks nicer
mail = Mail(app)




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)


from flaskblog.models import *

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Post=Post)