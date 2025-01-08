from flask import Blueprint

# Defina o Blueprint
auth_bp = Blueprint('auth', __name__)

# Rotas do Blueprint
@auth_bp.route('/login')
def login():
    return "Login Route"

@auth_bp.route('/register')
def register():
    return "Register Route"
