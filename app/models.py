
from tortoise import fields, Model


class BaseBlogModel(Model):
    """Base model for with standard field in models"""
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    is_active = fields.BooleanField(default=True)

    class Meta:
        abstract = True


class Post(BaseBlogModel):
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    owner = fields.ForeignKeyField(
        "models.User",
        related_name="posts",
        on_delete=fields.CASCADE
    )
    liked_by = fields.ManyToManyField(
        "models.User",
        through="Like",
        related_name="liked_posts",
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.title


class Like(BaseBlogModel):
    post = fields.ForeignKeyField("models.Post", related_name="likes", on_delete=fields.CASCADE)
    user = fields.ForeignKeyField(
        "models.User", related_name="likes", on_delete=fields.CASCADE
    )


class User(Model):
    # going to be implemented with FASTAPI-USERS
    name = fields.CharField(max_length=255)
