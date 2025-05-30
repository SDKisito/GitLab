from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_hello():
    response = client.get("/hello/DevOps")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour, DevOps !"}

def test_create_item():
    response = client.post("/items/", json={"name": "Laptop", "price": 999.99})
    assert response.status_code == 200
    assert "item_received" in response.json()
