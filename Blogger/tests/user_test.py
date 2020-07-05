import pytest
from project import db
from project.users.models import User

@pytest.fixture()
def init_db():
    print("---Fixture start---")
    db.create_all()
    user1=User('user1@gmail.com','user1','password123')
    user2=User('user2@gmail.com','user2','password1234')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    yield db

    db.drop_all()

def test_user1(init_db):
    first=User.query.get(1)
    assert first.username == 'user1'
