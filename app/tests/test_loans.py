import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.book import Base as BookBase
from app.models.user import Base as UserBase
from app.models.loan import Base as LoanBase

from app.schemas.book_schema import BookCreate
from app.schemas.user_schema import UserCreate
from app.schemas.loan_schema import LoanCreate

from app.services.book_service import BookService
from app.services.user_service import UserService
from app.services.loan_service import LoanService


# Banco de dados isolado para empréstimos
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

BookBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)
LoanBase.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    session = TestingSessionLocal()
    yield session
    session.close()


def setup_basic_objects(db):
    book_service = BookService(db)
    user_service = UserService(db)

    book = book_service.create_book(BookCreate(
        title="Livro Teste",
        author="Autor",
        year=2023,
        genres=["Fantasia"]
    ))

    user = user_service.create_user(UserCreate(
        name="Maria",
        email="maria@mail.com",
        registration="888"
    ))

    return user, book


def test_create_loan(db):
    loan_service = LoanService(db)
    user, book = setup_basic_objects(db)

    loan = loan_service.create_loan(LoanCreate(
        user_id=user.id,
        book_id=book.id
    ))

    assert loan.user_id == user.id
    assert loan.book_id == book.id
    assert loan.return_date is None


def test_user_max_loans_limit(db):
    loan_service = LoanService(db)
    user, book = setup_basic_objects(db)

    # Criar 3 livros diferentes
    book_svc = BookService(db)
    books = []
    for i in range(3):
        books.append(book_svc.create_book(BookCreate(
            title=f"Livro {i}",
            author="Autor",
            year=2020,
            genres=["Ação"]
        )))

    # Fazer 3 empréstimos
    for b in books:
        loan_service.create_loan(LoanCreate(user_id=user.id, book_id=b.id))

    # 4º empréstimo deve falhar
    with pytest.raises(Exception):
        loan_service.create_loan(LoanCreate(
            user_id=user.id,
            book_id=book.id
        ))


def test_return_book(db):
    loan_service = LoanService(db)
    user, book = setup_basic_objects(db)

    loan = loan_service.create_loan(LoanCreate(
        user_id=user.id,
        book_id=book.id
    ))

    result = loan_service.return_book(loan.id)

    assert result.return_date is not None
