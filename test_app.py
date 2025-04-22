import pytest
from s import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_addition_form_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Add Two Numbers" in response.data

def test_addition_post_valid(client):
    response = client.post('/', data={'num1': '2', 'num2': '3'})
    assert b"Result: 5.0" in response.data

def test_addition_post_invalid(client):
    response = client.post('/', data={'num1': 'a', 'num2': '3'})
    assert b"Invalid input" in response.data
