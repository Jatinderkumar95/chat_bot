import uuid
from base import BaseModel
from db import db

class Conversation(BaseModel):
    __tablename__ = "conversations"
    id : str = db.column(db.String,primary_key=True,default=lambda:str(uuid.uuid4),nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    messages = db.relationship("Message",back_populate="conversation",order_by="Message.created_on")