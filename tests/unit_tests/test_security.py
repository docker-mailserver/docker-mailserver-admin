from requests.exceptions import HTTPError

from .conftest import DOCKER_MAILSERVER_ADMIN_API_KEY

def test_admin_change_password_fails_if_api_key_is_missing(test_client):
    response = test_client.post(
        "/api/admin/v1/users/any_user/changePassword",
        json={
            "newPassword": "awesome_password",
        }
    )

    assert response.status_code == 403

def test_admin_change_password_fails_if_api_key_is_incorrect(test_client):
    response = test_client.post(
        "/api/admin/v1/users/any_user/changePassword",
        json={
            "newPassword": "awesome_password",
        },
        headers={
            "X-API-KEY": DOCKER_MAILSERVER_ADMIN_API_KEY + "_nope"
        }
    )

    assert response.status_code == 401