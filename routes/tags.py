from flask import Blueprint, request, jsonify
from models import db, Recipe, Tag

tags_bp = Blueprint('tags', __name__)

@tags_bp.route('/tags', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.to_dict() for tag in tags])

@tags_bp.route('/recipes/<int:recipe_id>/tags', methods=['POST'])
def add_tag_to_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json
    
    tag = Tag.query.filter_by(name=data['name'].lower()).first()
    if not tag:
        tag = Tag(name=data['name'].lower())
        db.session.add(tag)
    
    if tag not in recipe.tags:
        recipe.tags.append(tag)
        db.session.commit()
    
    return jsonify(tag.to_dict()), 201