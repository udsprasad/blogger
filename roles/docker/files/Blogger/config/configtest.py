from project import Basedir
import os
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(Basedir,'test.db')
SQLALCHEMY_TRACK_MODIFICATIONS=False
