from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Inicializar o banco de dados e migrações
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprints
    from .routes.auth import auth_bp
    from .routes.groups import groups_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(groups_bp, url_prefix='/groups')
    
    return app
