from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Freelancer, db

freelancer_bp = Blueprint('freelancer', __name__)

@freelancer_bp.route('/api/freelancers', methods=['GET'])
@jwt_required()
def get_freelancers():
    try:
        current_user_id = get_jwt_identity()
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
        return jsonify(freelancers_list), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar freelancers: {str(e)}"}), 500