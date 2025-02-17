from flask import Blueprint, request, jsonify
from flask_cors import cross_origin  # Import necessário para usar @cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Freelancer, db

freelancer_bp = Blueprint('freelancer', __name__)

# Rota para buscar freelancers
@freelancer_bp.route('/api/freelancers', methods=['GET'])
@jwt_required()
@cross_origin()
def get_freelancers():
    print("Recebendo requisição GET para freelancers")
    
    try:
        current_user_id = get_jwt_identity()  # Identidade do usuário no token
        print("ID do usuário:", current_user_id)  # Verificando a identidade do usuário
        
        freelancers = Freelancer.query.filter_by(user_id=current_user_id).all()
        freelancers_list = [{
            'id': freelancer.id,
            'nome_completo': freelancer.nome_completo,
            'celular': freelancer.celular,
            'sexo': freelancer.sexo,
            'email': freelancer.email,
            'rg': freelancer.rg,
            'chave_pix': freelancer.chave_pix
        } for freelancer in freelancers]
        
        print("Freelancers encontrados:", freelancers_list)
        return jsonify(freelancers_list), 200
    except Exception as e:
        print("Erro ao buscar freelancers:", str(e))
        return jsonify({"error": "Erro ao buscar freelancers"}), 500

# Rota para adicionar freelancers
@freelancer_bp.route('/api/freelancers', methods=['POST'])
@cross_origin()  # Habilita CORS para essa rota
def handle_freelancer():

    # Método POST - Adicionar freelancer
    if request.method == "POST":
        return add_freelancer()
    
@app.route("/api/freelancers", methods=["OPTIONS"])
@cross_origin()
def handle_options():
    # Configura o cabeçalho de resposta para permitir a requisição
    response = jsonify({})
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

def add_freelancer():
    try:
        current_user_id = get_jwt_identity()  # Obter a identidade do usuário a partir do JWT
        data = request.get_json()  # Obter os dados da requisição

        nome_completo = data.get('nome_completo')
        celular = data.get('celular')
        sexo = data.get('sexo')
        email = data.get('email')
        rg = data.get('rg')
        chave_pix = data.get('chave_pix')

        # Validação de campos obrigatórios
        if not nome_completo or not celular or not sexo or not email or not rg or not chave_pix:
            return jsonify({"error": "Todos os campos são obrigatórios"}), 400

        # Criação do freelancer no banco de dados
        new_freelancer = Freelancer(
            user_id=current_user_id,
            nome_completo=nome_completo,
            celular=celular,
            sexo=sexo,
            email=email,
            rg=rg,
            chave_pix=chave_pix
        )
        db.session.add(new_freelancer)
        db.session.commit()

        return jsonify({"message": "Freelancer adicionado com sucesso"}), 201

    except Exception as e:
        return jsonify({"error": f"Erro ao adicionar freelancer: {str(e)}"}), 500
