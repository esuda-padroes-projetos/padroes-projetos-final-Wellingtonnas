from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    registration = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False)  # aluno, professor, admin
