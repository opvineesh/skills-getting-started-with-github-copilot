def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_keys = {"Chess Club", "Programming Class", "Gym Class"}

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_keys.issubset(body.keys())
    for activity_name in expected_keys:
        assert "description" in body[activity_name]
        assert "schedule" in body[activity_name]
        assert "max_participants" in body[activity_name]
        assert "participants" in body[activity_name]
