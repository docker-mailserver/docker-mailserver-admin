import os
import pytest
from docker_mailserver_admin_api import app
from fastapi.testclient import TestClient

DOCKER_MAILSERVER_ADMIN_API_KEY = "testing_key!"
os.environ["DOCKER_MAILSERVER_ADMIN_API_KEY"] = DOCKER_MAILSERVER_ADMIN_API_KEY

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app=app)