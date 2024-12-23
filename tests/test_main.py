import pytest
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

@pytest.fixture
def single_transaction():
    return [{
        "items": [
            {
                "category": "Groceries",
                "amount": 50.00
            }
        ],
        "date": "2024-12-23"
    }]

@pytest.fixture
def multiple_transactions():
    return [
        {
            "items": [
                {
                    "category": "Groceries",
                    "amount": 50.00
                },
                {
                    "category": "Entertainment",
                    "amount": 30.00
                }
            ],
            "date": "2024-12-23"
        },
        {
            "items": [
                {
                    "category": "Dining",
                    "amount": 75.00
                },
                {
                    "category": "Entertainment",
                    "amount": 40.00
                }
            ],
            "date": "2024-12-23"
        }
    ]

def test_analyze_transactions_empty():
    response = client.post("/analyze-transactions", json=[])
    # TODO: implement assertion

def test_analyze_transactions_single(single_transaction):
    response = client.post("/analyze-transactions", json=single_transaction)
    # TODO: implement assertion

def test_analyze_transactions_multiple(multiple_transactions):
    response = client.post("/analyze-transactions", json=multiple_transactions)
    # TODO: implement assertion