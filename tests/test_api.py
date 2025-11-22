from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_play_endpoint_no_files():
    response = client.post("/play")
    assert response.status_code == 422  # parámetros faltantes
