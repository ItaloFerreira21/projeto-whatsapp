from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User, db

# Defina o Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])

def register():
    try:
        # Obter dados da requisição
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Dados inválidos, o corpo da requisição deve ser JSON"}), 400

        username = data.get("username")
        password = data.get("password")

        # Validação dos dados
        if not username or not password:
            return jsonify({"error": "Username e senha são obrigatórios"}), 400
        
        # Opcional: Validar critérios mínimos de senha
        if len(password) < 8:
            return jsonify({"error": "A senha deve ter pelo menos 8 caracteres"}), 400
        
        # Verificar se o usuário já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "Usuário já existe"}), 400
        
        # Criar um novo usuário
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuário criado com sucesso"}), 201

    except Exception as e:
        # Capturar erros inesperados
        return jsonify({"error": f"Erro interno no servidor: {str(e)}"}), 500


# Rotas do Blueprint
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        # Obter dados da requisição 
        data = request.get_json()
        if not isinstance(data, dict):
            return jsonify({"error": "Dados inválidos, o corpo da requisição deve ser JSON"}), 400

        username = data.get("username")
        password = data.get("password")

        # Validação dos dados simples
        if not username or not password:
            return jsonify({"error": "Usuário e senha são obrigatórios"}), 400
        
        # Verificar se o usuário existe e a senha está correta
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Usuário ou senha incorretos"}), 401

        # Criar um token JWT
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200

    except Exception as e:
        # Capturar erros inesperados
        return jsonify({"error": f"Erro interno no servidor: {str(e)}"}), 500        
        


