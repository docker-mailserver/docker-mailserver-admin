from subprocess import CompletedProcess
from .conftest import DOCKER_MAILSERVER_ADMIN_API_KEY


def test_admin_change_password_calls_bash_and_returns_200(test_client, mocker):
    user_to_modify = "any_user"
    new_password = "awesome_password"

    mocked_run = mocker.patch("subprocess.run")
    mocked_run.return_value = CompletedProcess(args=[], returncode=0)

    response = test_client.post(
        f"/api/admin/v1/users/{user_to_modify}/changePassword",
        json={
            "newPassword": new_password,
        },
        headers={
            "X-API-KEY": DOCKER_MAILSERVER_ADMIN_API_KEY
        }
    )

    assert response.status_code == 204

    used_args = mocked_run.call_args_list[0].args
    assert used_args[0] == ['./setup.sh', 'email', 'update', user_to_modify, new_password]