import pytest
from project import app as flask_app
import app
from tests.models_test import init_db
from project.contacts.models import Contacts

@pytest.fixture
def client():
    return flask_app.test_client()

def test_home_page(client,init_db):
    response=client.get('/')
    assert response.status_code==200
    assert b'about' in response.data
    assert b'contact' in response.data
    assert b'search'  in response.data

def test_about_page(client):
    response=client.get('/about')
    assert response.status_code==200

def test_contact_page(client,init_db):
    # testing GET
    response=client.get('/contacts/add_contact')
    assert response.status_code==200

    # testing POST
    reponse=client.post('/contacts/add_contact',data=dict(name='prasad',email='user1@gmail.com',phone_no='7999999999',msg='hii'),follow_redirects=True)
    assert response.status_code==200

def test_edit_page(client,init_db):
    response=client.get('/posts/edit/1')
    assert response.status_code==200

def test_register_page(client):
    # testing GET
    response=client.get('/user/register')
    assert response.status_code==200

    response=client.post('/user/register',data=dict(email='user123@gmail.com',username='user123',password='password123',password_confirm='password123'),follow_redirects=True)
    assert response.status_code==200

def test_login_page(client):
    # testing GET
    response=client.get('/login')
    assert response.status_code==200
    # testing POST
    response=client.post('/login',data=dict(email='prasad@gmail.com',password='password'),follow_redirects=True)
    assert response.status_code == 200
    assert b'Heyy you successfully logged in' in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data


    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"you logged out" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data
