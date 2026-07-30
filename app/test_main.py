from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_calculate_add():
    response = client.post("/calculate", json={"operation": "add", "a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}
