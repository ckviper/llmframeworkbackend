from models.chat import ChatHistoryResponse
from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter()

@router.get("/api/v1/chat/{chatId}", response_model=ChatHistoryResponse)
async def get_chat_history(chatId: UUID, db: Session = Depends(get_db)):
    chat_service = ChatService(db)
    return chat_service.get_chat_history(chatId)

@router.delete("/api/v1/chat/{chatId}")
async def delete_chat(chatId: UUID, db: Session = Depends(get_db)):
    chat_service = ChatService(db)
    chat_service.delete(chatId)
