from base64 import encode
from hashlib import sha256

from fastapi import FastAPI

from app.models import User
from app.schemas import UserSchema
from app.service import UserService

app = FastAPI()


@app.get("/{user_id}")
async def test(user_id: int):
    user = User.get(id=user_id)
    return UserSchema(user)


@app.post("/user/signup")
async def user_signup(user: UserSchema):
    return await UserService.signup_user(user)


@app.post("/user/login")
async def user_login():
    pass


@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int):
    user = User.get(id=user_id)
    return UserSchema(user)


@app.get("/user/{user_id}/activity")
async def last_activity(user_id: int):
    pass


@app.post("/post")
async def post_create():
    pass


@app.get("/post")
async def post_list():
    pass


@app.get("/post/{post_id}")
async def get_post(post_id: int):
    pass


@app.post("/post/{post_id}/like")
async def like_or_unlike_post(post_id: int):
    pass


@app.get("analytics")
async def get_like_analytics():
    pass
