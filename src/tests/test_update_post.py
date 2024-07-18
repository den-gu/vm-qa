import requests

BASE_URL = "http://localhost:80"

def get_token():
    url = f"{BASE_URL}/token"
    payload = {
        "username": "testuser",
        "password": "password"
    }
    response = requests.post(url, json=payload)
    return response.json()["token"]

def test_update_post():
    # Create a post first
    post_url = f"{BASE_URL}/posts"
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "title": "Post para Atualizar",
        "content": "Conteúdo do post"
    }
    create_response = requests.post(post_url, json=payload, headers=headers)
    post_id = create_response.json()["id"]

    # Update the post
    url = f"{BASE_URL}/posts/{post_id}"
    update_payload = {
        "title": "Post Atualizado",
        "content": "Conteúdo atualizado"
    }
    response = requests.put(url, json=update_payload, headers=headers)
    assert response.status_code == 200
