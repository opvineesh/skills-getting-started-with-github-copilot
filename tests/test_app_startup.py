from src import app as app_module


def test_app_has_expected_title():
    # Arrange
    expected_title = "Mergington High School API"

    # Act
    app_title = app_module.app.title

    # Assert
    assert app_title == expected_title


def test_app_mounts_static_route():
    # Arrange
    expected_path = "/static"

    # Act
    static_paths = [route.path for route in app_module.app.routes]

    # Assert
    assert expected_path in static_paths
