from sqlalchemy import false

from app.models.request import RequestCreate, RequestResponse
from app.database.models import Chat, Message
from sqlalchemy.dialects.postgresql import UUID
from app.core.config import settings
from fastapi.responses import JSONResponse
from app.models.response import Response
import requests


class RequestService:



    def __init__(self, db):
        self.db = db

    def create_request(self, request_data: RequestCreate) -> Response:
        response = self.send_message(request_data)

        chat = Chat(
            user_id=request_data.user_id,
            context= response.context.__str__()
        )

        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)

        message = Message(
            user_id=request_data.user_id,
            chat_id=chat.id,
            content=response.response
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return response

    def create_request_with_chat(self, chatid: int, request_data: RequestCreate) -> Response:
        response = self.send_message(request_data)

        message = Message(
            user_id=request_data.user_id,
            chat_id=chatid,
            content=response.response
        )

        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return response



    def send_message(self, request_data: RequestCreate) -> Response:
        payload = request_data.dict()
        payload['stream'] = False

        remote_url = settings.ollama_url + settings.generate_url

        response = requests.post(url=remote_url, json=payload)

        response = Response.parse_obj(response.json())
        return response
