from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
import json
import os

Basedir=os.path.abspath(os.path.dirname(__name__))

with open(Basedir+'/project/config.json', 'r') as c:
    params = json.load(c)["params"]



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = params['file_uploader']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL= True,
    MAIL_USERNAME = params['gmail_user'],
    MAIL_PASSWORD = params['gmail_password']
)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(Basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='mykeyy'

db = SQLAlchemy(app)
Migrate(app,db)

from project.posts.views import posts_blueprint
from project.contacts.views import contacts_blueprint

app.register_blueprint(posts_blueprint,url_prefix='/posts')
app.register_blueprint(contacts_blueprint,url_prefix='/contacts')
