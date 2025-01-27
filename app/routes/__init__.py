from flask import Blueprint

# Importar os Blueprints
from .auth import auth_bp
from .freelancer import freelancer_bp

# Definir uma lista de Blueprints para facilitar o registro
all_blueprints = [
    (auth_bp, '/auth'),
    (freelancer_bp, '/freelancer')
]

def register_blueprints(app):
    for bp, url_prefix in all_blueprints:
        app.register_blueprint(bp, url_prefix=url_prefix)