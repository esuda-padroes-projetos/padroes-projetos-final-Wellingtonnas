from sqlalchemy.orm import Session
from app.services.book_service import BookService
from app.services.user_service import UserService
from app.services.loan_service import LoanService
from app.schemas.book_schema import BookCreate, BookUpdate
from app.schemas.user_schema import UserCreate, UserUpdate
from app.schemas.loan_schema import LoanCreate


class LibraryFacade:
    def __init__(self, db: Session):
        self.book_service = BookService(db)
        self.user_service = UserService(db)
        self.loan_service = LoanService(db)

    # BOOKS ---------------------------------------------------------
    def list_books(self):
        return self.book_service.list_books()

    def create_book(self, data: BookCreate):
        return self.book_service.create_book(data)

    def update_book(self, book_id: int, data: BookUpdate):
        return self.book_service.update_book(book_id, data)

    def delete_book(self, book_id: int):
        return self.book_service.delete_book(book_id)

    def find_books_by_genre(self, genre: str):
        return self.book_service.find_by_genre(genre)

    # USERS ----------------------------------------------------------
    def list_users(self):
        return self.user_service.list_users()

    def create_user(self, data: UserCreate):
        return self.user_service.create_user(data)

    def update_user(self, user_id: int, data: UserUpdate):
        return self.user_service.update_user(user_id, data)

    def delete_user(self, user_id: int):
        return self.user_service.delete_user(user_id)

    # LOANS ----------------------------------------------------------
    def list_loans(self):
        return self.loan_service.list_loans()

    def create_loan(self, data: LoanCreate):
        return self.loan_service.create_loan(data)

    def return_book(self, loan_id: int):
        return self.loan_service.return_book(loan_id)
