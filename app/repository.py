from tortoise import Model

from app.models import User, BaseBlogModel, Post, Like


class BaseRepo:
    model: BaseBlogModel

    @classmethod
    async def get(cls, id: int) -> Model | None:
        return await cls.model.filter(is_active=True).get_or_none(id=id)

    @classmethod
    async def add(cls, payload: dict) -> Model:
        return await cls.model.create(**payload)

    @classmethod
    async def get_all(cls) -> list[Model]:
        return await cls.model.filter(is_active=True)

    @classmethod
    async def update(cls, payload: dict) -> Model:
        return await cls.model.update_from_dict(payload)

    @classmethod
    async def delete(cls, id: int) -> None:
        obj = await cls.model.get_or_none(id=id)
        obj.is_active = False
        await obj.save()


class UserRepo(BaseRepo):
    model = User


class PostRepo(BaseRepo):
    model = Post


class LikeRepo(BaseRepo):
    model = Like

    @classmethod
    async def delete(cls, id: int) -> None:
        obj = await cls.model.get_or_none(id=id)
        await obj.delete()

