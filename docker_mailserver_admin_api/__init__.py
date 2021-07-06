from fastapi import FastAPI

from .routers.admin import users

SETUP_SCRIPT_PATH = ""  # TODO: decide how to call

app = FastAPI()
app.include_router(users.router)
