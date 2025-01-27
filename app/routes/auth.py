from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User, db
import logging
# Configurar logging
logging.basicConfig(level=logging.DEBUG)

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
        email = data.get("email")
        password = data.get("password")
        confirmPassword = data.get("confirmPassword")
        cnpj = data.get("cnpj")
        company_name = data.get("company_name")
        phone_number = data.get("phone_number")

        # Validação dos dados
        if not username or not email or not password or not cnpj:
            return jsonify({"error": "Username, email, senha e CNPJ são obrigatórios"}), 400
        
        # Opcional: Validar critérios mínimos de senha
        if len(password) < 8:
            return jsonify({"error": "A senha deve ter pelo menos 8 caracteres"}), 400
        
        if password != confirmPassword:
            return jsonify({"error": "As senhas não conferem"}), 400
        
        # Verificar se o usuário já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "Usuário já existe"}), 400
        
        # Verificar se o email já existe
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return jsonify({"error": "Email já existe"}), 400
        
        # Verificar se o CNPJ já existe
        existing_cnpj = User.query.filter_by(cnpj=cnpj).first()
        if existing_cnpj:
            return jsonify({"error": "CNPJ já existe"}), 400
        
        # Criar um novo usuário
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password, cnpj=cnpj, company_name=company_name, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuário criado com sucesso"}), 201

    except Exception as e:
        logging.error(f"Erro interno no servidor: {str(e)}")
        # Capturar erros inesperados
        return jsonify({"error": f"Erro interno no servidor: {str(e)}"}), 500

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

# Exemplo de rota protegida
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({"message": f"Bem-vindo, {user.username}!"}), 200


