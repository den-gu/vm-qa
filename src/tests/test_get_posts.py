import requests

BASE_URL = "http://localhost:80"

def test_list_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url)
    assert response.status_code == 200
