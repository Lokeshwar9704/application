from app import app

def test_hello-world():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b'hello, Jenkins!'