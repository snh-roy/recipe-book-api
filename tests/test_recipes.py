import pytest
import json
from models import Recipe, db, User

@pytest.fixture
def sample_recipe(app, sample_user):
    """Create a sample recipe for tests"""
    with app.app_context():
        recipe = Recipe(
            name="Chocolate Cake",
            instructions="Mix and bake",
            prep_time=20,
            cook_time=30,
            user_id=sample_user
        )
        db.session.add(recipe)
        db.session.commit()
        recipe_id = recipe.id
    return recipe_id

class TestRecipes:
    def test_create_recipe_simple(self, client, sample_user):
        """Test creating a basic recipe"""
        recipe_data = {
            'name': 'Pasta Carbonara',
            'instructions': 'Cook pasta. Add eggs and cheese.',
            'prep_time': 10,
            'cook_time': 15,
            'user_id': sample_user
        }
        
        response = client.post('/recipes',
            data=json.dumps(recipe_data),
            content_type='application/json'
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == 'Pasta Carbonara'
        assert data['prep_time'] == 10
        assert 'id' in data
    
    def test_create_recipe_with_ingredients(self, client, sample_user):
        """Test creating recipe with ingredients"""
        recipe_data = {
            'name': 'Pancakes',
            'instructions': 'Mix ingredients and cook',
            'user_id': sample_user,
            'ingredients': [
                {'name': 'flour', 'quantity': '2 cups'},
                {'name': 'eggs', 'quantity': '2'},
                {'name': 'milk', 'quantity': '1 cup'}
            ]
        }
        
        response = client.post('/recipes',
            data=json.dumps(recipe_data),
            content_type='application/json'
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert len(data['ingredients']) == 3
        assert any(ing['ingredient'] == 'flour' for ing in data['ingredients'])
    
    def test_create_recipe_with_tags(self, client, sample_user):
        """Test creating recipe with tags"""
        recipe_data = {
            'name': 'Quick Salad',
            'instructions': 'Chop and mix',
            'user_id': sample_user,
            'tags': ['vegetarian', 'quick', 'healthy']
        }
        
        response = client.post('/recipes',
            data=json.dumps(recipe_data),
            content_type='application/json'
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert len(data['tags']) == 3
        assert any(tag['name'] == 'vegetarian' for tag in data['tags'])
    
    def test_get_all_recipes(self, client, sample_recipe):
        """Test retrieving all recipes"""
        response = client.get('/recipes')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1
    
    def test_get_recipe_by_id(self, client, sample_recipe):
        """Test retrieving specific recipe with full details"""
        response = client.get(f'/recipes/{sample_recipe}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == 'Chocolate Cake'
        assert 'ingredients' in data
        assert 'tags' in data
    
    def test_update_recipe(self, client, sample_recipe):
        """Test updating a recipe"""
        update_data = {
            'name': 'Super Chocolate Cake',
            'prep_time': 25
        }
        
        response = client.put(f'/recipes/{sample_recipe}',
            data=json.dumps(update_data),
            content_type='application/json'
        )
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == 'Super Chocolate Cake'
        assert data['prep_time'] == 25
        assert data['cook_time'] == 30  # Should remain unchanged
    
    def test_delete_recipe(self, client, sample_recipe):
        """Test deleting a recipe"""
        response = client.delete(f'/recipes/{sample_recipe}')
        
        assert response.status_code == 204
        
        # Verify it's really gone
        get_response = client.get(f'/recipes/{sample_recipe}')
        assert get_response.status_code == 404
    
    def test_search_by_ingredient(self, client, sample_user):
        """Test searching recipes by ingredient"""
        # Create recipe with specific ingredient
        recipe_data = {
            'name': 'Tomato Soup',
            'instructions': 'Cook tomatoes',
            'user_id': sample_user,
            'ingredients': [{'name': 'tomatoes', 'quantity': '4'}]
        }
        client.post('/recipes', data=json.dumps(recipe_data), content_type='application/json')
        
        response = client.get('/recipes/search?ingredient=tomato')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1
        assert any(recipe['name'] == 'Tomato Soup' for recipe in data)
    
    def test_search_by_tag(self, client, sample_user):
        """Test searching recipes by tag"""
        recipe_data = {
            'name': 'Vegan Curry',
            'instructions': 'Cook vegetables',
            'user_id': sample_user,
            'tags': ['vegan', 'indian']
        }
        client.post('/recipes', data=json.dumps(recipe_data), content_type='application/json')
        
        response = client.get('/recipes/search?tag=vegan')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1
        assert any(recipe['name'] == 'Vegan Curry' for recipe in data)
    
    def test_create_recipe_invalid_user(self, client):
        """Test creating recipe with non-existent user"""
        recipe_data = {
            'name': 'Orphan Recipe',
            'instructions': 'Should fail',
            'user_id': 9999
        }
        
        response = client.post('/recipes',
            data=json.dumps(recipe_data),
            content_type='application/json'
        )
        
        # This will likely fail! Need to add validation
        assert response.status_code in [400, 404]