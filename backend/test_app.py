from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_hello():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello World!"}


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
