import pytest
from project import db
from project.users.models import User,check_password_hash
from project.posts.models import Posts

@pytest.fixture()
def init_db():
    db.create_all()
    user=User('user1@gmail.com','user1','password123')
    post=Posts(title='nature',slug='peace',tagline='superbb',content='hai nature is cool',date='7/6/2020',img_name='pic.jpg')
    db.session.add(user)
    db.session.add(post)
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
