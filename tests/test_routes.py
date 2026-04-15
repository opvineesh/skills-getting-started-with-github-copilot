def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_shape(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert len(body) > 0
    for _, activity in body.items():
        assert required_fields.issubset(activity.keys())
