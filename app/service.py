from typing import TypeVar

from pydantic import BaseModel
from tortoise import Model

from app.repository import UserRepo
from app.schemas import UserSchema
from core.auth.auth_handler import sign_jwt


ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)


class Service:
    model: Model
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    query_schema: QuerySchemaType
    get_schema: GetSchemaType

    async def create(self, schema: UserSchema):
        user = await UserRepo.add(self.create_schema.dict())
        return


class UserService():

    @staticmethod
    async def signup_user(user: UserSchema):
        await UserRepo.add(user.dict())
        return sign_jwt(user.email)

    @staticmethod
    async def get_all():
        await UserRepo.get_all()

