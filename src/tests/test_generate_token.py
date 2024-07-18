import requests

BASE_URL = "http://localhost"

def test_generate_token():
    url = f"{BASE_URL}/token"
    payload = {
        "username": "user",
        "password": "pass123"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
