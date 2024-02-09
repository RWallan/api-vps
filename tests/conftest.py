import pytest
from fastapi.testclient import TestClient

from api_vps.app import app


@pytest.fixture
def client():
    return TestClient(app=app)
