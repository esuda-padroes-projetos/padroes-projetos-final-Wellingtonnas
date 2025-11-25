import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.book import Base as BookBase
from app.services.book_service import BookService
from app.schemas.book_schema import BookCreate, BookUpdate

# Banco em memória para testes
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BookBase.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_book(db):
    service = BookService(db)
    data = BookCreate(
        title="Dom Quixote",
        author="Miguel de Cervantes",
        year=1605,
        genres=["Romance"]
    )
    book = service.create_book(data)
    assert book.title == "Dom Quixote"


def test_update_book(db):
    service = BookService(db)

    # Primeiro cria
    book = service.create_book(
        BookCreate(
            title="Livro Teste",
            author="Autor",
            year=2020,
            genres=["Ficção"]
        )
    )

    # Depois atualiza
    updated = service.update_book(
        book.id,
        BookUpdate(
            title="Livro Alterado",
            author="Autor",
            year=2021,
            genres=["Drama"]
        )
    )

    assert updated.title == "Livro Alterado"
    assert updated.year == 2021


def test_find_books_by_genre(db):
    service = BookService(db)

    service.create_book(BookCreate(
        title="Livro A",
        author="X",
        year=2020,
        genres=["Terror"]
    ))

    result = service.find_by_genre("Terror")
    assert len(result) == 1
