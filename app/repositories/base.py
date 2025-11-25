from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session
from app.models.base import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get_by_id(self, db: Session, item_id: int):
        return db.query(self.model).filter(self.model.id == item_id).first()

    def delete(self, db: Session, item_id: int):
        obj = self.get_by_id(db, item_id)
        if obj:
            db.delete(obj)
            db.commit()
            return True
        return False
