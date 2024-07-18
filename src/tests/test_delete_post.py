import requests

BASE_URL = "http://localhost:80"

def get_token():
    url = f"{BASE_URL}/token"
    user = {
        "username": "user",
        "password": "pass123"
    }
    response = requests.post(url, json=user)
    return response.json()["token"]

def test_delete_post():
    # Create a post first
    post_url = f"{BASE_URL}/posts/"
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    post = {
        "title": "Post que vai ser apagado",
        "content": "Lorem ispum dolor sit amet"
    }
    create_response = requests.post(post_url, json=post, headers=headers)
    post_id = create_response.json()["id"]

    # Delete the post
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
