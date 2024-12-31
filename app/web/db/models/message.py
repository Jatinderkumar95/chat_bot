import uuid
from app.web.db import db
from base import BaseModel

class Message(BaseModel):
    id: str = db.Column(
        db.String(), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    role: str = db.Column(db.String, nullable=False)
    content: str = db.Column(db.String, nullable=False)
    conversation_id:str = db.Column(db.String,db.ForeignKey("conversations.id"),nullable=False)
    conversation = db.relationship("Conversation",back_populates="messages")
