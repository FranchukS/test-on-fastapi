from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "user" ADD "is_active" INT NOT NULL  DEFAULT 1;
        ALTER TABLE "user" ADD "email" VARCHAR(255) NOT NULL;
        ALTER TABLE "user" ADD "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "user" RENAME COLUMN "name" TO "nickname";
        ALTER TABLE "user" ADD "last_activity" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;
        ALTER TABLE "user" ADD "hash_password" VARCHAR(255) NOT NULL;
        ALTER TABLE "user" ADD "last_login" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME COLUMN "nickname" TO "name";
        ALTER TABLE "user" ADD "name" VARCHAR(255) NOT NULL;
        ALTER TABLE "user" DROP COLUMN "updated_at";
        ALTER TABLE "user" DROP COLUMN "is_active";
        ALTER TABLE "user" DROP COLUMN "email";
        ALTER TABLE "user" DROP COLUMN "created_at";
        ALTER TABLE "user" DROP COLUMN "last_activity";
        ALTER TABLE "user" DROP COLUMN "hash_password";
        ALTER TABLE "user" DROP COLUMN "last_login";"""
