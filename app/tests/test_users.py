import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.user import Base as UserBase
from app.services.user_service import UserService
from app.schemas.user_schema import UserCreate, UserUpdate

engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
UserBase.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_user(db):
    service = UserService(db)

    user = service.create_user(UserCreate(
        name="Ana",
        email="ana@email.com",
        registration="123"
    ))

    assert user.name == "Ana"


def test_update_user(db):
    service = UserService(db)

    user = service.create_user(UserCreate(
        name="João",
        email="joao@email.com",
        registration="555"
    ))

    updated = service.update_user(
        user.id,
        UserUpdate(
            name="João Silva",
            email="joao@email.com",
            registration="555"
        )
    )

    assert updated.name == "João Silva"


def test_prevent_duplicate_email(db):
    service = UserService(db)

    service.create_user(UserCreate(
        name="Usuário 1",
        email="user@mail.com",
        registration="001"
    ))

    with pytest.raises(Exception):
        service.create_user(UserCreate(
            name="Usuário 2",
            email="user@mail.com",
            registration="002"
        ))
