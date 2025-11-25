# app/utils/validators.py

from datetime import date
from fastapi import HTTPException, status

def validate_string(field_name: str, value: str, min_length: int = 1):
    """
    Valida se um campo string não é vazio e atende ao tamanho mínimo.
    """
    if not isinstance(value, str) or len(value.strip()) < min_length:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} deve ter pelo menos {min_length} caracteres."
        )


def validate_positive_int(field_name: str, value: int):
    """
    Valida números inteiros positivos.
    """
    if not isinstance(value, int) or value <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} deve ser um número positivo."
        )


def validate_date_order(start_date: date, end_date: date):
    """
    Valida se a data de empréstimo é anterior à data de devolução.
    """
    if start_date > end_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A data de devolução não pode ser anterior à data de empréstimo."
        )
