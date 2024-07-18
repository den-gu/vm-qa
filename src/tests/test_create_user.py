import requests

BASE_URL = "http://localhost:80"

def test_create_user():
    url = f"{BASE_URL}/users"
    payload = {
        "username": "user2",
        "password": "pass123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["username"] == "user2"
