import pytest
from project import app as flask_app
import app
from tests.models_test import init_db

@pytest.fixture
def client():
    return flask_app.test_client()

def test_home_page(client,init_db):
    response=client.get('/')
    assert response.status_code==200
    assert b'Web Blogger'in response.data

def test_about_page(client):
    response=client.get('/about')
    assert response.status_code==200

def test_contact_page(client,init_db):
    response=client.get('/contacts/add_contact')
    assert response.status_code==200

def test_login_page(client):
    response=client.get('/login')
    assert response.status_code==200

def test_edit_page(client,init_db):
    response=client.get('/posts/edit/1')
    assert response.status_code==200

def test_register_page(client):
    response=client.get('/user/register')
    assert response.status_code==200
