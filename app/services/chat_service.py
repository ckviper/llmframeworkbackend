from typing import List

from app.database.models import Message
from app.models.message import MessageModel


class ChatService:
    def __init__(self, db):
        self.db = db


    def get_all_chat_messages(self, chat_id : int) -> List[Message]:
        entities = self.db.query(Message).filter(Message.chat_id == chat_id).all()

        messages = [MessageModel(id=entity.id, message=entity.content) for entity in entities]
        return messages



