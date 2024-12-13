from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .database import Base
from uuid import uuid4
from datetime import datetime


class Request(Base):
    __tablename__ = "requests"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"))
    model = Column(String, index=True)
    message = Column(String)
    temperature = Column(Float, default=0.7)
    created_at = Column(DateTime, default=datetime.utcnow)
