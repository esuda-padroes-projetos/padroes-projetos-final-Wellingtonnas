from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def list_users(self):
        return self.repo.get_all()

    def get_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        return user

    def create_user(self, data: UserCreate):
        exists = self.repo.get_by_email(data.email)
        if exists:
            raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

        return self.repo.create(
            name=data.name,
            email=data.email,
            registration=data.registration
        )

    def update_user(self, user_id: int, data: UserUpdate):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        updated = self.repo.update(user, data)
        return updated

    def delete_user(self, user_id: int):
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        self.repo.delete(user)
        return {"message": "Usuário removido com sucesso."}
