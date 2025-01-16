from flask import jsonify, request
from app import app, db
from models import User

@app.route('/users', methods=['GET'])
def get_users():
    """
    Retorna uma lista de todos os usuários cadastrados.
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Retorna os detalhes de um usuário específico pelo ID.
    """
    user = User.query.get(id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    """
    Cria um novo usuário no banco de dados.
    """
    data = request.get_json()

    errors = User.validate_user(data)
    if errors:
        return jsonify({'errors': errors}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """
    Atualiza os dados de um usuário existente.
    """
    user = User.query.get(id)
    data = request.get_json()
    
    if not user:
        return jsonify({"error": "User not found"}), 404

    errors = User.validate_user(data, is_update=True)
    if errors:
        return jsonify({'errors': errors}), 400

    if 'email' in data:
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user and existing_user.id != id:
            return jsonify({"error": "Email already exists"}), 400

    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']

    db.session.commit()
    return jsonify(user.to_dict()), 200 

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """
    Remove um usuário do banco de dados pelo ID.
    """
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
    