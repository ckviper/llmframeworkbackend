from models.request import RequestCreate, RequestResponse
from database.chat import Message, Chat
from sqlalchemy.dialects.postgresql import UUID
from fastapi.responses import JSONResponse


class RequestService:
    def __init__(self, db):
        self.db = db

    def create_request(self, request_data: RequestCreate) -> RequestResponse:
        chat = Chat(
            user_id=request_data.user_id,  
            model=request_data.model,      
            context=None,                  
        )
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)

        message = Message(
            chat_id=chat.id,
            user_id=request_data.user_id,  
            message=request_data.message,
            temperature=request_data.temperature,
        )
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return RequestResponse(
            chat_id=chat.id,
            response="Ответ от нейронки", 
            created_at=message.creation_timestamp,
        ) 

    def create_request_with_chat(self, chatid: UUID, request_data: RequestCreate) -> RequestRespons:
        #chat = self.db.query(Chat).filter(Chat.id == chatid).first()
        
        message = Message(
            chat_id=chatid,
            user_id=request_data.user_id,  
            message=request_data.message,
            temperature=request_data.temperature,
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)

        return RequestResponse(
            chat_id=chatid,
            response="Ответ от нейронки",
            created_at=message.created_at,
        )