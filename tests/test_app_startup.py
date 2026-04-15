from src import app as app_module


def test_app_title_is_expected():
    # Arrange
    expected_title = "Mergington High School API"

    # Act
    app_title = app_module.app.title

    # Assert
    assert app_title == expected_title


def test_static_mount_route_exists():
    # Arrange
    expected_path = "/static"

    # Act
    route_paths = [route.path for route in app_module.app.routes]

    # Assert
    assert expected_path in route_paths
