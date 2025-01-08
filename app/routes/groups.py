from flask import Blueprint

# Definindo o Blueprint
groups_bp = Blueprint('groups', __name__)

# Adicionando rotas ao Blueprint
@groups_bp.route('/groups')
def list_groups():
    return "List of Groups"

@groups_bp.route('/groups/create')
def create_group():
    return "Create a Group"
