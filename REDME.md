Projeto WhatsApp
Este é um projeto de backend para um sistema de autenticação de usuários usando Flask, SQLAlchemy, PostgreSQL e JWT.

Requisitos
Python 3.10 ou superior
PostgreSQL
Virtualenv (opcional, mas recomendado)
Configuração do Ambiente de Desenvolvimento
1. Clone o repositório
git clone https://github.com/seu-usuario/projeto-whatsapp.git
cd projeto-whatsapp

2. Crie e ative um ambiente virtual
No Linux/MacOS
python3 -m venv venv
source venv/bin/activate

No Windows
python -m venv venv
venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure o banco de dados PostgreSQL
Crie o banco de dados:

Conecte-se ao PostgreSQL e crie um banco de dados chamado userswpp:
psql -U postgres

No prompt do PostgreSQL:
CREATE DATABASE userswpp;
\q

Configure as variáveis de ambiente:
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=supersecrectkey
SQLALCHEMY_DATABASE_URI=postgresql://postgres:172421@localhost:5432/userswpp
SQLALCHEMY_TRACK_MODIFICATIONS=False
JWT_SECRET_KEY=super-secret

Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:

5. Inicialize o banco de dados
Inicialize as migrações:
flask db init

Crie uma nova migração:
flask db migrate -m "Initial migration"

Aplique a migração ao banco de dados:
flask db upgrade

6. Execute o servidor Flask
flask run

O servidor estará em execução em http://localhost:5000.

Endpoints da API
Registro de Usuário
URL: /auth/register
Método: POST
Body: JSON
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "testpass",
    "confirmPassword": "testpass"
}

Login de Usuário
URL: /auth/login
Método: POST
Body: JSON
{
    "username": "testuser",
    "password": "testpass"
}
Consultas SQL
Listar todos os usuários
SELECT * FROM "user";

Listar todos os registros
SELECT * FROM "record";

Ferramentas Recomendadas
Clientes de Banco de Dados GUI
pgAdmin: Download pgAdmin
DBeaver: Download DBeaver
DataGrip: Download DataGrip
Extensões para VS Code
PostgreSQL: Instalar PostgreSQL Extension
SQLTools: Instalar SQLTools Extension
git clone https://github.com/seu-usuario/projeto-whatsapp.git
cd projeto-whatsapp