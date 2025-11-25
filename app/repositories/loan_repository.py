from app.models.loan import Loan
from app.models.book import Book
from app.models.user import User

class LoanRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.query(Loan).all()

    def get_by_id(self, loan_id: int):
        return self.db.query(Loan).filter(Loan.id == loan_id).first()

    def get_active_loans_by_user(self, user_id: int):
        return self.db.query(Loan).filter(
            Loan.user_id == user_id,
            Loan.return_date == None
        ).all()

    def get_active_loans_by_book(self, book_id: int):
        return self.db.query(Loan).filter(
            Loan.book_id == book_id,
            Loan.return_date == None
        ).first()

    def create(self, loan: Loan):
        self.db.add(loan)
        self.db.commit()
        self.db.refresh(loan)
        return loan

    def update(self, loan: Loan):
        self.db.commit()
        self.db.refresh(loan)
        return loan
