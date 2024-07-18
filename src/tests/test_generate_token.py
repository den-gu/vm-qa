import requests

BASE_URL = "http://localhost"

def test_generate_token():
    url = f"{BASE_URL}/token"
    user = {
        "username": "user",
        "password": "pass123"
    }
    response = requests.post(url, json=user)
    assert response.status_code == 200
