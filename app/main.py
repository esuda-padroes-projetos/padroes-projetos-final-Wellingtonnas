from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.book_controller import router as book_router
from app.controllers.user_controller import router as user_router
from app.controllers.loan_controller import router as loan_router

from app.models.book import Base as BookBase
from app.models.user import Base as UserBase
from app.models.loan import Base as LoanBase
from app.factories.db_manager import engine

# Criar tabelas automaticamente
BookBase.metadata.create_all(bind=engine)
UserBase.metadata.create_all(bind=engine)
LoanBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Biblioteca API",
    description="API completa para gerenciamento de usuários, livros e empréstimos",
    version="1.0"
)

# Liberar requisições do front-end
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rotas
app.include_router(book_router)
app.include_router(user_router)
app.include_router(loan_router)

@app.get("/")
def root():
    return {"message": "API da Biblioteca está online!"}
