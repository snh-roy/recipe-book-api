from flask import Blueprint, request, jsonify
from models import db, Recipe, Ingredient, RecipeIngredient

ingredients_bp = Blueprint('ingredients', __name__)

@ingredients_bp.route('/ingredients', methods=['GET'])
def get_ingredients():
    ingredients = Ingredient.query.all()
    return jsonify([ing.to_dict() for ing in ingredients])

@ingredients_bp.route('/recipes/<int:recipe_id>/ingredients', methods=['POST'])
def add_ingredient_to_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json
    
    # Get or create ingredient
    ingredient = Ingredient.query.filter_by(name=data['name'].lower()).first()
    if not ingredient:
        ingredient = Ingredient(name=data['name'].lower())
        db.session.add(ingredient)
        db.session.flush()
    
    # Add to recipe
    recipe_ing = RecipeIngredient(
        recipe_id=recipe.id,
        ingredient_id=ingredient.id,
        quantity=data.get('quantity', '')
    )
    db.session.add(recipe_ing)
    db.session.commit()
    
    return jsonify(recipe_ing.to_dict()), 201

@ingredients_bp.route('/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
def remove_ingredient_from_recipe(recipe_id, ingredient_id):
    recipe_ing = RecipeIngredient.query.filter_by(
        recipe_id=recipe_id,
        ingredient_id=ingredient_id
    ).first_or_404()
    
    db.session.delete(recipe_ing)
    db.session.commit()
    return '', 204