from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange
    app_module.activities = deepcopy(INITIAL_ACTIVITIES)
    yield


@pytest.fixture
def client():
    # Arrange
    with TestClient(app_module.app) as test_client:
        yield test_client
