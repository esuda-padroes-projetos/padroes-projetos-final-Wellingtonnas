from app.models.book import Book
from app.models.book import Genre

class BookFactory:
    @staticmethod
    def create(title="Livro Padrão", author="Autor Padrão", year=2024, genres=None):
        if genres is None:
            genres = ["Ficção"]

        genre_objects = [Genre(name=g) for g in genres]

        return Book(
            title=title,
            author=author,
            year=year,
            genres=genre_objects
        )
