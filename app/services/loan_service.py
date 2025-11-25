from fastapi import HTTPException
from datetime import date

from app.models.loan import Loan
from app.repositories.loan_repository import LoanRepository
from app.repositories.user_repository import UserRepository
from app.repositories.book_repository import BookRepository
from app.schemas.loan_schema import LoanCreate

class LoanService:
    MAX_LOANS_PER_USER = 3

    def __init__(self, db):
        self.db = db
        self.repo = LoanRepository(db)
        self.users = UserRepository(db)
        self.books = BookRepository(db)

    def list_loans(self):
        return self.repo.get_all()

    def create_loan(self, data: LoanCreate):
        # 1 — Verificar se o usuário existe
        user = self.users.get_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        # 2 — Verificar se o livro existe
        book = self.books.get_by_id(data.book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Livro não encontrado.")

        # 3 — Verificar se o usuário já está com 3 livros
        active_loans = self.repo.get_active_loans_by_user(user.id)
        if len(active_loans) >= self.MAX_LOANS_PER_USER:
            raise HTTPException(
                status_code=400,
                detail="Usuário já está com o limite máximo de 3 livros."
            )

        # 4 — Verificar se o livro já está emprestado
        book_loan = self.repo.get_active_loans_by_book(book.id)
        if book_loan:
            raise HTTPException(
                status_code=400,
                detail="Este livro já está emprestado."
            )

        # 5 — Criar empréstimo
        loan = Loan(
            user_id=data.user_id,
            book_id=data.book_id,
            loan_date=date.today(),
            return_date=None
        )

        return self.repo.create(loan)

    def return_book(self, loan_id: int):
        loan = self.repo.get_by_id(loan_id)
        if not loan:
            raise HTTPException(status_code=404, detail="Empréstimo não encontrado.")

        if loan.return_date:
            raise HTTPException(status_code=400, detail="Este livro já foi devolvido.")

        loan.return_date = date.today()
        return self.repo.update(loan)
