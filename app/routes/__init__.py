from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .auth import auth_bp
#from .routes.groups import groups_bp  # Certifique-se de que isso está correto

# Inicialize extensões (SQLAlchemy e Migrate)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Use o caminho do banco que desejar
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar o Blueprint de autenticação
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
