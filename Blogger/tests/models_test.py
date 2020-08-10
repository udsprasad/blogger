import pytest
import os
from project import db,create_app
from project.users.models import User,check_password_hash
from project.posts.models import Posts
from project.contacts.models import Contacts
from flask_sqlalchemy import SQLAlchemy

config_obj=os.environ.get('DIAG_CONFIG_MODULE','config.configtest')
app=create_app(config_obj)
db.init_app(app)
app.app_context().push()


@pytest.fixture()
def init_db():
    db.create_all()
    user=User('user1@gmail.com','user1','password123')
    post=Posts(title='nature',slug='peace',tagline='superbb',content='hai nature is cool',date='7/6/2020',img_name='pic.jpg')
    contact=Contacts(name='user1',email='user1@gmail.com',phone_no='7999999999',msg='hiiii')
    db.session.add(user)
    db.session.add(post)
    db.session.add(contact)
    db.session.commit()
    yield db
    db.drop_all()

def test_user1(init_db):
    first=User.query.get(1)
    assert first.username == 'user1'
    assert first.email == 'user1@gmail.com'
    assert check_password_hash(first.password_hash,'password123')

def test_post(init_db):
    first=Posts.query.get(1)
    assert first.title=='nature'
    assert first.slug=='peace'
    assert first.tagline=='superbb'
    assert first.content=='hai nature is cool'
    assert first.date=='7/6/2020'
    assert first.img_name=='pic.jpg'

def test_contact(init_db):
    first=Contacts.query.get(1)
    assert first.name=='user1'
    assert first.email=='user1@gmail.com'
    assert first.phone_no=='7999999999'
    assert first,msg=='hiiii'
