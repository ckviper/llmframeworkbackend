from fastapi import FastAPI
from app.database.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()