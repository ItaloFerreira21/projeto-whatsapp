from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import User, db
import logging

# Configurar logging
logging.basicConfig(level=logging.DEBUG)

def register_user(request):
    try:
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirmPassword = data.get("confirmPassword")
        cnpj = data.get("cnpj")
        company_name = data.get("company_name")
        phone_number = data.get("phone_number")

        if not username or not email or not password or not cnpj:
            return jsonify({"error": "Username, email, senha e CNPJ são obrigatórios"}), 400
        
        if len(password) < 8:
            return jsonify({"error": "A senha deve ter pelo menos 8 caracteres"}), 400
        
        if password != confirmPassword:
            return jsonify({"error": "As senhas não conferem"}), 400
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"error": "Usuário já existe"}), 400
        
        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            return jsonify({"error": "Email já existe"}), 400
        
        existing_cnpj = User.query.filter_by(cnpj=cnpj).first()
        if existing_cnpj:
            return jsonify({"error": "CNPJ já existe"}), 400
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password, cnpj=cnpj, company_name=company_name, phone_number=phone_number)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Usuário criado com sucesso"}), 201

    except Exception as e:
        logging.error(f"Erro interno no servidor: {str(e)}")
        return jsonify({"error": f"Erro interno no servidor: {str(e)}"}), 500

def login_user(request):
    try:
        data = request.get_json()
        logging.debug(f"Dados recebidos: {data}")
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"error": "Usuário e senha são obrigatórios"}), 400
        
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"error": "Usuário ou senha incorretos"}), 401

        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200

    except Exception as e:
        logging.error(f"Erro interno no servidor: {str(e)}")
        return jsonify({"error": f"Erro interno no servidor: {str(e)}"}), 500