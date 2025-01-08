# Rotas da aplicação

""" from flask import Blueprint, request, jsonify

routes = Blueprint("routes", __name__)

# Lista os critérios disponíveis para seleção de participantes
@routes.route("/list-criteria", methods=["GET"])
def list_criteria():
    criteria = [
        "Os mais ativos",
        "Por ordem de disponibilidade",
        "Por gênero",
        "Aleatório"
    ]
    return jsonify({"criteria": criteria})

# Endpoint para criar um grupo no WhatsApp
@routes.route("/create-group", methods=["POST"])
def create_group():
    data = request.json
    group_name = data.get("group_name")
    number_of_participants = data.get("number_of_participants")
    criteria = data.get("criteria")

    # Validação básica
    if not group_name or not number_of_participants or not criteria:
        return jsonify({"error": "Dados incompletos"}), 400

    # Aqui adicionaremos a lógica de criação de grupo futuramente
    return jsonify({
        "message": "Grupo criado com sucesso!",
        "group_name": group_name,
        "number_of_participants": number_of_participants,
        "criteria": criteria
    })
 """