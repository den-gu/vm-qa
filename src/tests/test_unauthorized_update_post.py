import requests

BASE_URL = "http://localhost:80"

def get_token(username, password):
    url = f"{BASE_URL}/token"
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    return response.json()["token"]

def test_unauthorized_update():
    # Create a post with user
    post_url = f"{BASE_URL}/posts"
    token_user1 = get_token("user", "pass123")
    headers_user1 = {
        "Authorization": f"Bearer {token_user1}"
    }
    payload = {
        "title": "Post de user",
        "content": "Lorem ispum dolor sit amet"
    }
    create_response = requests.post(post_url, json=payload, headers=headers_user1)
    post_id = create_response.json()["id"]

    # Try to update the post with user2
    token_user2 = get_token("user2", "pass123")
    headers_user2 = {
        "Authorization": f"Bearer {token_user2}"
    }
    update_payload = {
        "title": "Tentanto Atualizar o Post do User1",
        "content": "Conteúdo não autorizado"
    }
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.put(url, json=update_payload, headers=headers_user2)
    assert response.status_code == 403
