from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import json
import os
from flask_login import LoginManager

login_manager=LoginManager()

Basedir=os.path.abspath(os.path.dirname(__name__))

with open(Basedir+'/project/config.json', 'r') as c:
    params = json.load(c)["params"]

db = SQLAlchemy()

def create_app(configfile):
    app=Flask(__name__)
    app.config.from_object(configfile)
    return app
config_obj=os.environ.get('DIAG_CONFIG_MODULE','config.configapp')
app=create_app(config_obj)
app.config['UPLOAD_FOLDER'] = Basedir+'/project/static/uploads'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL= True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)
db.init_app(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view='login'

from project.posts.views import posts_blueprint
from project.contacts.views import contacts_blueprint
from project.users.views import user_blueprint

app.register_blueprint(posts_blueprint,url_prefix='/posts')
app.register_blueprint(contacts_blueprint,url_prefix='/contacts')
app.register_blueprint(user_blueprint,url_prefix='/user')
