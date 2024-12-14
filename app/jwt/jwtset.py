from app.core.config import AUTH_JWT_SECRET_KEY
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = AUTH_JWT_SECRET_KEY
