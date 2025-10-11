from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from models import db, User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    
    # Validate required fields
    if not data.get('name'):
        return jsonify({'error': 'name is required'}), 400
    if not data.get('email'):
        return jsonify({'error': 'email is required'}), 400
    
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    
    try:
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'}), 409

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())