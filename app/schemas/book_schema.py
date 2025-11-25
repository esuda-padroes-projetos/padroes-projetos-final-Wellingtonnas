from typing import List, Optional
from pydantic import BaseModel
from .base import BaseSchema


class GenreSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    genres: Optional[List[str]] = []


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    genres: Optional[List[str]] = None


class Book(BookBase, BaseSchema):
    genres: List[GenreSchema] = []
