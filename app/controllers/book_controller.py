from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.factories.db_manager import get_db
from app.services.book_service import BookService
from app.schemas.book_schema import BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def list_books(db: Session = Depends(get_db)):
    service = BookService(db)
    return service.list_books()


@router.get("/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.get_book(book_id)


@router.post("/")
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.create_book(data)


@router.put("/{book_id}")
def update_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.update_book(book_id, data)


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.delete_book(book_id)


@router.get("/genre/{genre_name}")
def find_by_genre(genre_name: str, db: Session = Depends(get_db)):
    service = BookService(db)
    return service.find_by_genre(genre_name)
