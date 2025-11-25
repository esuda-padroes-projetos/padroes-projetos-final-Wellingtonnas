from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import BookCreate, BookUpdate
from app.models.book import Genre

class BookService:
    def __init__(self, db: Session):
        self.repo = BookRepository(db)

    def list_books(self):
        return self.repo.get_all()

    def get_book(self, book_id: int):
        book = self.repo.get_by_id(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Livro não encontrado.")
        return book

    def create_book(self, data: BookCreate):
        genres = [Genre(name=name) for name in data.genres]
        return self.repo.create(
            title=data.title,
            author=data.author,
            year=data.year,
            genres=genres
        )

    from app.repositories.book_repository import BookRepository

class BookService:
    def __init__(self, db):
        self.db = db
        self.repo = BookRepository()  # sem DB aqui!

    def list_books(self):
        return self.repo.get_all(self.db)

    def get_book(self, book_id: int):
        return self.repo.get_by_id(self.db, book_id)

    def delete_book(self, book_id: int):
        return self.repo.delete(self.db, book_id)

