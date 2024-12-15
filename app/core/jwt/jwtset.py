from app.core.config import AUTH_JWT_SECRET_KEY
from pydantic import BaseModel
from fastapi import HTTPException
from functools import wraps
from fastapi_jwt_auth import AuthJWT


class Settings(BaseModel):
    authjwt_secret_key: str = AUTH_JWT_SECRET_KEY


# Декоратор для защиты маршрутов
def jwt_required_decorator(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        Authorize: AuthJWT = kwargs.get("Authorize")
        if Authorize is None:
            raise HTTPException(status_code=403 , detail="AuthJWT dependency is required")
        # Проверяем JWT токен
        try:
            Authorize.jwt_required()
        except Exception as e:
            raise HTTPException(status_code=401, detail="Invalid or missing token")     
        return await func(*args, **kwargs)
    return wrapper
