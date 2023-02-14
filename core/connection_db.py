from tortoise.contrib.fastapi import register_tortoise

import settings
from api.api import app


def connect_database():
    register_tortoise(
        app=app,
        config=settings.DB_CONFIG,
    )
