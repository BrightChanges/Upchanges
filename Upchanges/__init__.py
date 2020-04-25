# To connect all the codes in Upchanges's folder to run the application(app.py)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

# DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    'data.sqlite')  # Taking risk by using mysql, maysbe should had use sqlite.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

db = SQLAlchemy(app)
Migrate(app, db)

# SET UP LOGIN CONFIGURATION
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

# IMPORTING BLUEPRINTS FROM VIEWS.PY FILE IN OTHER FOLDERS
from Upchanges.core.views import core
from Upchanges.users.views import users
from Upchanges.error_pages.handlers import error_pages
from Upchanges.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
