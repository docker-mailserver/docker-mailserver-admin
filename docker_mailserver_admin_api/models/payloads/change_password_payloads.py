from pydantic import BaseModel, Field


class AdminChangePasswordPayload(BaseModel):
    new_password: str = Field(..., alias="newPassword")
