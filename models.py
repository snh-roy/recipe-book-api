from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Junction table for Recipe-Tags (many-to-many)
recipe_tags = db.Table('recipe_tags',
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    recipes = db.relationship('Recipe', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    prep_time = db.Column(db.Integer)  # minutes
    cook_time = db.Column(db.Integer)  # minutes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    recipe_ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True, cascade='all, delete-orphan')
    tags = db.relationship('Tag', secondary='recipe_tags', backref='recipes')
    
    def to_dict(self, include_details=False):
        data = {
            'id': self.id,
            'name': self.name,
            'instructions': self.instructions,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat()
        }
        if include_details:
            data['ingredients'] = [ri.to_dict() for ri in self.recipe_ingredients]
            data['tags'] = [tag.to_dict() for tag in self.tags]
        return data

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

class RecipeIngredient(db.Model):
    """Junction table fixing the duplicate ingredient issue"""
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.String(50))  # e.g., "2 cups", "1 tablespoon"
    
    ingredient = db.relationship('Ingredient')
    
    def to_dict(self):
        return {
            'ingredient': self.ingredient.name,
            'quantity': self.quantity
        }

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }