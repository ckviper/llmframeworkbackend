from models.request import RequestCreate, RequestResponse
from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from database.database import get_db
from services.request_service import RequestService  

router = APIRouter()

@router.post("/api/v1/request", response_model=RequestResponse)
async def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    request_service = RequestService(db)
    return request_service.create_request(request)


@router.post("/api/v1/request/{chatId}", response_model=RequestResponse)
async def create_request_with_chat(chatId: UUID, request: RequestCreate, db: Session = Depends(get_db)):
    request_service = RequestService(db)
    return request_service.create_request_with_chat(chatId, request)

