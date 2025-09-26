from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Sample recipient address (replace with testnet/ganache/Hardhat account)
RECIPIENT = "0x1234567890abcdef1234567890abcdef12345678"


def test_root():
    """Check root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Public Funds Transparency MVP Running" in response.json()["message"]


def test_allocation_default():
    """By default, allocation should be 0"""
    response = client.get(f"/funds/allocation/{RECIPIENT}")
    assert response.status_code == 200
    assert response.json()["allocation"] == 0


def test_allocate_funds(monkeypatch):
    """Simulate allocation transaction"""
    def mock_allocate_funds(recipient, amount):
        return {"tx_hash": "0xFAKETX123"}

    monkeypatch.setattr("app.services.fund_service.allocate_funds", mock_allocate_funds)

    response = client.post(f"/funds/allocate/{RECIPIENT}/1000")
    assert response.status_code == 200
    assert "tx_hash" in response.json()


def test_mark_complete(monkeypatch):
    """Simulate marking project complete"""
    def mock_mark_project_complete(recipient):
        return {"tx_hash": "0xFAKETX456"}

    monkeypatch.setattr("app.services.fund_service.mark_project_complete", mock_mark_project_complete)

    response = client.post(f"/funds/mark-complete/{RECIPIENT}")
    assert response.status_code == 200
    assert "tx_hash" in response.json()


def test_release_funds(monkeypatch):
    """Simulate releasing funds"""
    def mock_release_funds(recipient):
        return {"tx_hash": "0xFAKETX789"}

    monkeypatch.setattr("app.services.fund_service.release_funds", mock_release_funds)

    response = client.post(f"/funds/release/{RECIPIENT}")
    assert response.status_code == 200
    assert "tx_hash" in response.json()
