import subprocess
from http import HTTPStatus

from fastapi import APIRouter, Depends, Response
from fastapi.security import APIKeyHeader

from ...models.payloads import AdminChangePasswordPayload
from ...security import check_api_key

router = APIRouter(dependencies=[Depends(check_api_key)])


@router.post(
    "/api/admin/v1/users/{email_address}/changePassword",
    status_code=HTTPStatus.NO_CONTENT,
    response_class=Response,
)
async def change_password(email_address: str, body: AdminChangePasswordPayload):
    result = subprocess.run(
        ["setup", "email", "update", email_address, body.new_password]
    )
    result.check_returncode()  # NOTE: safeguard this
