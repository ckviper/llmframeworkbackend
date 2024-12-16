from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class Chat(BaseModel):
    id: int = Field(description="Индивидуальный идентификатор чата")
    user_id: int = Field(description="Индентификатор юзера")
    model: str = Field(description="Модель с которой работаем")
    message: str = Field(description="Сообщение в чате")


class ChatCreate(BaseModel):
    user_id: int = Field(description="Индентификатор юзера")
    model: str = Field(description="Модель с которой работаем")
    message: str


class ChatResponse(BaseModel):
    id: UUID = Field(description="Индивидуальный идентификатор чата")
    user_id: int = Field(description="Индентификатор юзера")
    model: str = Field(description="Модель с которой работаем")
    message: str = Field(description="Сообщение в чате")
    created_at: datetime = Field(description="Время отправленного запроса")


class ChatHistoryResponse(BaseModel):
    model: str = Field(description="Модель с которой работаем")
    messages: list[dict] = Field(description="История сообщений")