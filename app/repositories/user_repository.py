from sqlalchemy.orm import Session
from .base import BaseRepository
from app.models.user import User

class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_by_registration(self, db: Session, registration: str):
        return db.query(User).filter(User.registration == registration).first()
