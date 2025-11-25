from sqlalchemy.orm import Session
from .base import BaseRepository
from app.models.book import Book, Genre
from app.repositories.base import BaseRepository
from app.models.book import Book

class BookRepository(BaseRepository[Book]):
    def __init__(self):
        super().__init__(Book)

    def search(self, db: Session, text: str):
        text = f"%{text}%"
        return (
            db.query(Book)
            .filter(
                (Book.title.ilike(text)) |
                (Book.author.ilike(text))
            )
            .all()
        )

    def get_by_genre(self, db: Session, genre_name: str):
        return (
            db.query(Book)
            .join(Book.genres)
            .filter(Genre.name.ilike(genre_name))
            .all()
        )
