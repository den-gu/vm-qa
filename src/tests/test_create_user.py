import requests

BASE_URL = "http://localhost:80"

def test_create_user():
    url = f"{BASE_URL}/users/"
    user = {
        "username": "user2",
        "password": "pass123"
    }
    response = requests.post(url, json=user)
    assert response.status_code == 201
