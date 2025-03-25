import pytest
from app import app

# Add a blank line here ⬇️⬇️


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Add a blank line here ⬇️⬇️


def test_home(client):
    response = client.get("/")
    assert response.data == b"Hello, World!"

