import uvicorn
from fastapi import FastAPI
from app.database.database import engine, Base
from app.api.v1.endpoints.auth import router as auth_router
from fastapi_jwt_auth import AuthJWT
from app.core.jwt.jwtset import Settings

Base.metadata.create_all(bind=engine)


@AuthJWT.load_config
def get_config():
    return Settings()


app = FastAPI()

app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(f"app.{__name__}:app", host="0.0.0.0", port=8000, reload=True)

