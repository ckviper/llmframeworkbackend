from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .database import Base
from uuid import uuid4
from datetime import datetime


class Chat(Base):
    __tablename__ = "chats"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    context = Column(String, nullable=True)
    creation_timestamp = Column(DateTime, default=datetime.now(datetime.timezone.utc))

    messages = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), index=True)
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"), index=True)
    content = Column(String, nullable=False)
    creation_timestamp = Column(DateTime, default=datetime.now(datetime.timezone.utc))

    chat = relationship("Chat", back_populates="messages")