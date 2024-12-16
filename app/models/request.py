from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class Request(BaseModel):
    id: int = Field(description="Индивидуальный идентификатор запроса")
    chat_id: UUID = Field(description="Индивидуальный идентификатор чата")
    model: str = Field(description="Модель с которой работаем")
    message: str = Field(description="Сообщение отправленное пользователем")
    temperature: float = Field(default=0.7, description="Температура используемая для ответа от нейронки")
    created_at: datetime = Field(description="Время отправленного запроса")


class RequestCreate(BaseModel):
    user_id: UUID = Field(description="Идентификатор пользователя")
    model: str = Field(description="Модель нейронной сети")
    message: str = Field(description="Сообщение пользователя")
    temperature: float = Field(default=0.7, description="Температура для генерации ответа")


class RequestResponse(BaseModel):
    chat_id: UUID = Field(description="Уникальный идентификатор чата")
    response: str = Field(description="Ответ сообщение")
    created_at: datetime = Field(description="Время создания запроса")