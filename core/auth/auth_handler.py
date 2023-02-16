# This file is responsible for signing , encoding , decoding and returning JWTS
import time

import jwt

import settings
from settings import env

secret_key = env("JWT_SECRET")
algorithm = env("JWT_ALGORITHM")


def token_response(token: str):
    return {
        "access_token": token
    }

# function used for signing the JWT string
def sign_jwt(user_email: str) -> dict[str, str]:
    payload = {
        "user_email": user_email,
        "expires": time.time() + settings.TOKEN_EXPIRED_TIME
    }
    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=[algorithm])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
