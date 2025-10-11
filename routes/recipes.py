from flask import Blueprint, request, jsonify
from models import db, Recipe, Ingredient, RecipeIngredient, Tag, recipe_tags, User

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.json
    
    # Validate user exists
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': f'User with id {user_id} not found'}), 404
    
    # Validate required fields
    if not data.get('name'):
        return jsonify({'error': 'name is required'}), 400
    if not data.get('instructions'):
        return jsonify({'error': 'instructions is required'}), 400
    
    # Create recipe
    recipe = Recipe(
        name=data['name'],
        instructions=data['instructions'],
        prep_time=data.get('prep_time'),
        cook_time=data.get('cook_time'),
        user_id=user_id
    )
    db.session.add(recipe)
    db.session.flush()
    
    # Add ingredients
    if 'ingredients' in data:
        for ing_data in data['ingredients']:
            ingredient = Ingredient.query.filter_by(name=ing_data['name'].lower()).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_data['name'].lower())
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                quantity=ing_data.get('quantity', '')
            )
            db.session.add(recipe_ing)
    
    # Add tags
    if 'tags' in data:
        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name.lower()).first()
            if not tag:
                tag = Tag(name=tag_name.lower())
                db.session.add(tag)
            recipe.tags.append(tag)
    
    db.session.commit()
    return jsonify(recipe.to_dict(include_details=True)), 201

@recipes_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify(recipe.to_dict(include_details=True))

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    data = request.json
    
    recipe.name = data.get('name', recipe.name)
    recipe.instructions = data.get('instructions', recipe.instructions)
    recipe.prep_time = data.get('prep_time', recipe.prep_time)
    recipe.cook_time = data.get('cook_time', recipe.cook_time)
    
    db.session.commit()
    return jsonify(recipe.to_dict(include_details=True))

@recipes_bp.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return '', 204

@recipes_bp.route('/recipes/search', methods=['GET'])
def search_recipes():
    ingredient_name = request.args.get('ingredient')
    tag_name = request.args.get('tag')
    
    query = Recipe.query
    
    if ingredient_name:
        query = query.join(RecipeIngredient).join(Ingredient).filter(
            Ingredient.name.contains(ingredient_name.lower())
        )
    
    if tag_name:
        query = query.join(recipe_tags).join(Tag).filter(
            Tag.name == tag_name.lower()
        )
    
    recipes = query.all()
    return jsonify([recipe.to_dict() for recipe in recipes])


@recipes_bp.route('/seed', methods=['POST'])
def seed_database_endpoint():
    """Special endpoint to seed the database"""
    try:
        from _seed_data import seed_database
        seed_database()
        return jsonify({"message": "Database seeded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500