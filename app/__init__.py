from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

# Inicialize extensões (SQLAlchemy, Migrate, JWT e CORS)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True'
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    # Inicializar extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)  # Inicializar JWTManager com a aplicação Flask

    # Configurar o CORS para permitir o frontend específico
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

    # Adicionar cabeçalhos CORS manualmente para garantir que 'Access-Control-Allow-Credentials' seja verdadeiro
    @app.after_request
    def after_request(response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
        response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'  # Permite os headers necessários
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'  # Permite os métodos HTTP
        return response

    # Importar e registrar os Blueprints
    from app.routes import api_bp
    app.register_blueprint(api_bp)

    # Exibir as rotas registradas (útil para depuração)
    with app.app_context():
        print("Rotas registradas:")
        for rule in app.url_map.iter_rules():
            print(rule)

    return app

from app import models  # Importar modelos após a definição do objeto db
