# To connect all the codes in Upchanges's folder to run the application(upchanges.py)
import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, TimedSerializer
# from Upchanges.models import User, BlogPost, BlogProject, BlogInfo, BlogIdea, EmailConfirm,MangagePassword

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thispasswordwillnotworkanywhereelse123'

# DATABASE SETUP
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    '../Upchanges/data.sqlite')  # Taking risk by using mysql, maysbe should had use sqlite.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
# app.config.from_object(__name__)



#Need to changes the Mail Server, Gmail doesn't work

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') or 'AKIAXKIVF3IC7EMYCJFA'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') or 'BKnRSkA3+RVaJzUdqFQLM9lfxbAYLU6ilVNdghqru2fZ'
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER') or 'email-smtp.ap-northeast-1.amazonaws.com'
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT') or '465'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

s = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# connect_password = MangagePassword.query(1)
# mail_admin_password = connect_password.password
# print(mail_admin_password)         #Need to find a way to safely decrypt my password in a table and let this __init__.py read it and be able to log in to my Gmail account

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

db = SQLAlchemy(app)
Migrate(app, db)

# admin = Admin(app, name='Upchanges_admin_page', template_mode='bootstrap3')
# admin.add_view(ModelView(BlogPost, db.session))



# SET UP LOGIN CONFIGURATION
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

# IMPORTING BLUEPRINTS FROM VIEWS.PY FILE IN OTHER FOLDERS
from Upchanges.core.views import core
from Upchanges.core.vn_views import vn_core
from Upchanges.core.jp_views import jp_core
from Upchanges.core.usa_views import usa_core
from Upchanges.core.estonia_views import estonia_core
from Upchanges.core.ghana_views import ghana_core
from Upchanges.core.mongolia_views import mongolia_core
from Upchanges.core.other_countries import other_countries_core
from Upchanges.users.views import users
from Upchanges.error_pages.handlers import error_pages
from Upchanges.blog_posts.views import blog_posts
from Upchanges.blog_posts.vn_views import vn_blog_posts
from Upchanges.blog_posts.jp_views import jp_blog_posts
from Upchanges.blog_posts.usa_views import usa_blog_posts
from Upchanges.blog_posts.estonia_views import estonia_blog_posts
from Upchanges.blog_posts.ghana_views import ghana_blog_posts
from Upchanges.blog_posts.mongolia_views import mongolia_blog_posts
from Upchanges.blog_posts.other_countries import other_countries_blog_posts
#
# from Upchanges.blog_posts.other_countries import other_countries_blog_posts
from Upchanges.blog_info.views import blog_info


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(blog_posts)
app.register_blueprint(vn_core)
app.register_blueprint(jp_core)
app.register_blueprint(usa_core)
app.register_blueprint(estonia_core)
app.register_blueprint(ghana_core)
app.register_blueprint(mongolia_core)
app.register_blueprint(other_countries_core)
app.register_blueprint(vn_blog_posts)
app.register_blueprint(jp_blog_posts)
app.register_blueprint(usa_blog_posts)
app.register_blueprint(estonia_blog_posts)
app.register_blueprint(ghana_blog_posts)
app.register_blueprint(mongolia_blog_posts)
app.register_blueprint(other_countries_blog_posts)
#
# app.register_blueprint(other_countries_blog_posts)
app.register_blueprint(blog_info)


if not os.path.exists('logs'):
    os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/upchanges.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Upchanges startup')
    app.logger.info('Scheduler started')