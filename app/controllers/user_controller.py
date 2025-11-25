from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.factories.db_manager import get_db
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.list_users()


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user(user_id)


@router.post("/")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(data)


@router.put("/{user_id}")
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.update_user(user_id, data)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(user_id)
