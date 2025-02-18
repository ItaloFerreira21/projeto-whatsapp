from flask import Blueprint, jsonify, request
from app import db
from app.models import Freelancer
from flask_jwt_extended import jwt_required, get_jwt_identity

# Crie o Blueprint para agrupar as rotas
api_bp = Blueprint('api', __name__)

# Rota para listar todos os freelancers
@api_bp.route('/api/freelancers', methods=['GET', 'POST', 'OPTIONS'])
@jwt_required()  # Verifica se o token JWT está presente e é válido
def get_freelancers():
    if request.method == 'OPTIONS':
        return jsonify({'message': 'OK'}), 200

    try:
        # Recupera todos os freelancers do banco de dados
        freelancers = Freelancer.query.all()
        # Serializa os freelancers para enviar como resposta JSON
        freelancers_list = [
            {
                'id': freelancer.id,
                'nome_completo': freelancer.nome_completo,
                'celular': freelancer.celular,
                'sexo': freelancer.sexo,
                'email': freelancer.email,
                'rg': freelancer.rg,
                'chave_pix': freelancer.chave_pix
            }
            for freelancer in freelancers
        ]
        return jsonify(freelancers_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
