from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: reset mutable in-memory state so tests are isolated.
    app_module.activities = deepcopy(INITIAL_ACTIVITIES)
    yield


@pytest.fixture
def client():
    # Arrange: create API client for endpoint tests.
    with TestClient(app_module.app) as test_client:
        yield test_client
