from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.factories.db_manager import get_db
from app.services.loan_service import LoanService
from app.schemas.loan_schema import LoanCreate

router = APIRouter(prefix="/loans", tags=["Loans"])


@router.get("/")
def list_loans(db: Session = Depends(get_db)):
    service = LoanService(db)
    return service.list_loans()


@router.post("/")
def create_loan(data: LoanCreate, db: Session = Depends(get_db)):
    service = LoanService(db)
    return service.create_loan(data)


@router.put("/return/{loan_id}")
def return_book(loan_id: int, db: Session = Depends(get_db)):
    service = LoanService(db)
    return service.return_book(loan_id)
