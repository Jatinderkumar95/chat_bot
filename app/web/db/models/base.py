from db import db
from abc import abstractmethod

class BaseModel(db.Model):
    __abstract__ = True
    
    @classmethod
    def create():
        return
        #save()

    
    @abstractmethod
    def save():
        
        db.session.commit()
     
