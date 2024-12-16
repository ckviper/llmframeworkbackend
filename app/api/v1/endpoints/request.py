from app.models.request import RequestCreate, RequestResponse
from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.response import Response
from app.services.request_service import RequestService

router = APIRouter()

@router.post("/api/v1/request", response_model=Response)
async def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    request_service = RequestService(db)
    return request_service.create_request(request)


@router.post("/api/v1/request/{chatId}", response_model=Response)
async def create_request_with_chat(chatId: int, request: RequestCreate, db: Session = Depends(get_db)):
    request_service = RequestService(db)
    return request_service.create_request_with_chat(chatId, request)

