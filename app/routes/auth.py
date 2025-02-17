from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User, db
from app.services.auth_service import register_user, login_user

# Defina o Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    return register_user(request)

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user(request)



# Exemplo de rota protegida
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Bem-vindo, {user.username}!"}), 200


