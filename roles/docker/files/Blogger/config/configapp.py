#python configuration
from project import Basedir
import os
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(Basedir,'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY='mykeyy'
