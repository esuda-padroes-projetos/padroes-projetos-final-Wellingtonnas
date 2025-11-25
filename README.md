# 📚 Sistema de Gerenciamento de Biblioteca

Projeto Final — 2ª Avaliação  
Disciplina: **Padrões de Projeto**  
Alunos: **Nathalia Leite, Thiago Aragão e Wellington Carneiro Nascimento**

---

## 🚀 Sobre o Projeto

Este projeto é um sistema completo para gerenciamento de **livros**, **usuários** e **empréstimos**, desenvolvido utilizando:

- **Backend em Python (FastAPI)**
- **Frontend em JavaScript/HTML/CSS**
- **Banco de Dados SQLite**
- Arquitetura organizada em **Camadas** (Controllers → Services → Repositories → Database)
- Aplicando **Padrões de Projeto (1ª e 2ª Unidade)**

O objetivo é demonstrar domínio de desenvolvimento web, integração entre camadas, aplicação de padrões de projeto e boas práticas.

---

# 🏗️ Arquitetura do Sistema

frontend/
├── books.html
├── users.html
├── loans.html
└── utils.js

app/
├── main.py
├── controllers/
├── services/
├── repositories/
├── factories/
├── models/
└── database.db

Divisão em camadas favorece organização, escalabilidade e desacoplamento.

---

# 📌 Funcionalidades Principais (CRUD Completo)

### 📚 Livros

- Criar livro
- Listar livros
- Editar livro
- Excluir livro

### 👤 Usuários

- Criar usuário
- Listar usuários
- Excluir usuário

### 🔄 Empréstimos

- Registrar empréstimo
- Listar empréstimos
- Finalizar devolução

---

# 🧠 Padrões de Projeto Utilizados

## **🎯 Primeira Unidade — Padrões Criacionais e Estruturais**

### 🔨 **Factory Method**

- Utilizado no módulo `factories/db_manager.py`
- Cria e gerencia a instância do banco de dados (engine) de forma padronizada.

### 🏭 **Singleton**

- O engine do SQLAlchemy é único no sistema.
- Garantimos apenas uma instância para evitar inconsistências.

### 🧱 **Repository Pattern (Arquitetural)**

- `repositories/`
- Cada entidade possui um repositório responsável pelas operações no banco (CRUD).
- Remove SQL direto do controlador e melhora organização.

### 🧩 **Facade**

- Camada de **service** atua como uma fachada entre controllers e repositories.

---

## **🎯 Segunda Unidade — Padrões Comportamentais**

### 📏 **Strategy**

Aplicado indiretamente:  
Cada service utiliza estratégias diferentes para gerenciar entidades (livro, usuário, empréstimo).

### 🎬 **Command** (conceito aplicado)

Cada controller executa comandos específicos enviados ao service, simulando execução de ações.

### 🔍 **Observer** _(opcional, se quiser mencionar)_

O frontend fica “observando” mudanças na API através de requisições assíncronas.

---

# 🗄️ Banco de Dados

- Banco **SQLite**
- Geração automática das tabelas com SQLAlchemy
- Entidades:
  - Book
  - User
  - Loan

---

# ⚙️ Como Rodar o Projeto

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv

Ativar ambiente

Windows:

venv\Scripts\activate

Instalar dependências
pip install -r requirements.txt

Rodar servidor FastAPI
uvicorn app.main:app --reload

API ficará disponível em:

👉 http://127.0.0.1:8000

👉 http://127.0.0.1:8000/docs
 (Swagger)

 Abrir o Frontend

Basta abrir os arquivos HTML:

books.html

users.html

loans.html

Integração Frontend ↔ Backend

O frontend usa fetch() para consumir a API:

const API_BASE_URL = "http://127.0.0.1:8000";

estes Unitários

Foram criados testes para validar lógica de serviços e endpoints da API (2AV).

Conclusão

Este projeto demonstra:

✔ Arquitetura organizada
✔ CRUD completo
✔ Aplicação de múltiplos padrões de projeto
✔ Integração entre front, API e banco
✔ Uso profissional do GitHub
✔ Projeto pronto para apresentação 🎤

✨ Autores

Nathalia Leite

Thiago Aragão

Wellington Carneiro doNascimento
```
