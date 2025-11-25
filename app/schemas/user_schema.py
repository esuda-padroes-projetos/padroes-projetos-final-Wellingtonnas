from typing import Optional
from pydantic import BaseModel, EmailStr
from .base import BaseSchema


class UserBase(BaseModel):
    name: str
    email: EmailStr
    registration: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    registration: Optional[str] = None


class User(BaseSchema, UserBase):
    pass
