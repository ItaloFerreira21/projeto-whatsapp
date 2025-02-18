from flask import Blueprint

# Importar os Blueprints
from .freelancer import api_bp as freelancer_bp

# Definir uma lista de Blueprints para facilitar o registro
all_blueprints = [
    (freelancer_bp, '/api')
]

def register_blueprints(app):
    for bp, url_prefix in all_blueprints:
        app.register_blueprint(bp, url_prefix=url_prefix)