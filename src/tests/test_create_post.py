import requests

BASE_URL = "http://localhost:80"

def get_token():
    url = f"{BASE_URL}/token"
    user = {
        "username": "user",
        "password": "pass123"
    }
    response = requests.post(url, json=user)
    # response = json.loads(response_body)
    
    # return response.json()["token"]

def test_create_post():
    url = f"{BASE_URL}/posts"
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "title": "O mercado de criptomoedas",
        "content": "Lorem ispum dolor sit amet"
    }
    response = requests.post(url, json=user, headers=headers)
    assert response.status_code == 201
