from typing import List

from app.models.message import MessageModel
from app.models.chat import ChatHistoryResponse
from fastapi import APIRouter, Depends
from uuid import UUID
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.chat_service import ChatService

router = APIRouter()

@router.get("/api/v1/chat/{chatId}")
async def get_chat_history(chatId: int, db: Session = Depends(get_db)) -> List[MessageModel]:
    chat_service = ChatService(db)
    return chat_service.get_all_chat_messages(chatId)

@router.delete("/api/v1/chat/{chatId}")
async def delete_chat(chatId: int, db: Session = Depends(get_db)):
    chat_service = ChatService(db)
    chat_service.delete(chatId)
