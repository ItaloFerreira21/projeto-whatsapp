from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Inicialize extensões (SQLAlchemy, Migrate, JWT e CORS)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:172421@localhost:5432/userswpp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Adicione a chave secreta do JWT

    # Inicializar extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  # Inicializar JWTManager com a aplicação Flask
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})  # Permitir requisições de http://localhost:5173

    # Importar e registrar os Blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app

from app import models  # Importar modelos após a definição do objeto db