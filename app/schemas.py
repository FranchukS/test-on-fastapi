from datetime import datetime

from pydantic import BaseModel, Field


class BlogSchema(BaseModel):
    id: int = Field(None, description="ID")
    title: str = Field(None, description="Title")
    content: str = Field(None, description="Content")


    class Config:
        orm_mode = True


class LikeSchema(BaseModel):
    pass


class UserSchema(BaseModel):
    nickname: str = Field(default=None)
    email: str = Field(default=None)
    hash_password: str = Field(default=None)


class UserLoginSchema(BaseModel):
    email: str = Field(default=None)
    password: str = Field(default=None)
