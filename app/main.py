from fastapi import FastAPI
from app.database.database import engine, Base
from app.api.v1.endpoints.auth import router as auth_router
from fastapi_jwt_auth import AuthJWT
from app.jwt.jwtset import Settings

Base.metadata.create_all(bind=engine)


@AuthJWT.load_config
def get_config():
    return Settings()


app = FastAPI()

app.include_router(auth_router)
