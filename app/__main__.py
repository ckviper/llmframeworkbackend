import uvicorn
from fastapi import FastAPI
from app.database.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

