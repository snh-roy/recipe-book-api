from app import create_app
from models import db, User, Recipe, Ingredient, RecipeIngredient, Tag

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        print("🗑️  Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create users
        print("👥 Creating users...")
        users = [
            User(name="Gordon Ramsay", email="gordon@masterchef.com"),
            User(name="Julia Child", email="julia@cooking.com"),
            User(name="Jamie Oliver", email="jamie@food.com")
        ]
        db.session.add_all(users)
        db.session.commit()
        
        # Create tags
        print("🏷️  Creating tags...")
        tags_data = ['vegetarian', 'vegan', 'quick', 'dessert', 'italian', 'mexican', 'healthy', 'comfort-food']
        tags = {name: Tag(name=name) for name in tags_data}
        db.session.add_all(tags.values())
        db.session.commit()
        
        # Create recipes with ingredients
        print("🍳 Creating recipes...")
        
        # Recipe 1: Spaghetti Carbonara
        carbonara = Recipe(
            name="Spaghetti Carbonara",
            instructions="1. Cook spaghetti according to package. 2. Fry pancetta until crispy. 3. Mix eggs and parmesan. 4. Toss hot pasta with pancetta, then egg mixture. 5. Season with black pepper.",
            prep_time=10,
            cook_time=15,
            user_id=users[0].id
        )
        db.session.add(carbonara)
        db.session.flush()
        
        carbonara_ingredients = [
            ('spaghetti', '400g'),
            ('eggs', '4'),
            ('parmesan cheese', '100g'),
            ('pancetta', '200g'),
            ('black pepper', 'to taste')
        ]
        
        for ing_name, quantity in carbonara_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=carbonara.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        carbonara.tags.extend([tags['italian'], tags['comfort-food']])
        
        # Recipe 2: Avocado Toast
        avocado_toast = Recipe(
            name="Avocado Toast",
            instructions="1. Toast bread. 2. Mash avocado with lime juice. 3. Spread on toast. 4. Top with cherry tomatoes and red pepper flakes.",
            prep_time=5,
            cook_time=2,
            user_id=users[1].id
        )
        db.session.add(avocado_toast)
        db.session.flush()
        
        toast_ingredients = [
            ('bread', '2 slices'),
            ('avocado', '1'),
            ('lime', '1/2'),
            ('cherry tomatoes', '5'),
            ('red pepper flakes', 'pinch')
        ]
        
        for ing_name, quantity in toast_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=avocado_toast.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        avocado_toast.tags.extend([tags['vegetarian'], tags['quick'], tags['healthy']])
        
        # Recipe 3: Chocolate Chip Cookies
        cookies = Recipe(
            name="Chocolate Chip Cookies",
            instructions="1. Cream butter and sugars. 2. Beat in eggs and vanilla. 3. Mix in flour, baking soda, salt. 4. Fold in chocolate chips. 5. Bake at 375°F for 10 minutes.",
            prep_time=15,
            cook_time=10,
            user_id=users[2].id
        )
        db.session.add(cookies)
        db.session.flush()
        
        cookie_ingredients = [
            ('butter', '1 cup'),
            ('brown sugar', '3/4 cup'),
            ('white sugar', '3/4 cup'),
            ('eggs', '2'),
            ('vanilla extract', '2 tsp'),
            ('flour', '2 1/4 cups'),
            ('baking soda', '1 tsp'),
            ('salt', '1 tsp'),
            ('chocolate chips', '2 cups')
        ]
        
        for ing_name, quantity in cookie_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=cookies.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        cookies.tags.extend([tags['dessert'], tags['vegetarian']])
        
        # Recipe 4: Veggie Tacos
        tacos = Recipe(
            name="Black Bean Tacos",
            instructions="1. Sauté onions and peppers. 2. Add black beans and spices. 3. Warm tortillas. 4. Fill with bean mixture. 5. Top with salsa, avocado, and cilantro.",
            prep_time=10,
            cook_time=15,
            user_id=users[1].id
        )
        db.session.add(tacos)
        db.session.flush()
        
        taco_ingredients = [
            ('black beans', '2 cans'),
            ('bell peppers', '2'),
            ('onion', '1'),
            ('tortillas', '8'),
            ('avocado', '1'),
            ('salsa', '1 cup'),
            ('cilantro', '1/4 cup'),
            ('cumin', '1 tsp'),
            ('chili powder', '1 tsp')
        ]
        
        for ing_name, quantity in taco_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=tacos.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        tacos.tags.extend([tags['vegan'], tags['mexican'], tags['healthy']])
        
        # Recipe 5: Chicken Stir Fry
        stirfry = Recipe(
            name="Quick Chicken Stir Fry",
            instructions="1. Slice chicken and vegetables. 2. Heat wok with oil. 3. Cook chicken until done. 4. Add vegetables and stir fry. 5. Add soy sauce and serve over rice.",
            prep_time=20,
            cook_time=10,
            user_id=users[0].id
        )
        db.session.add(stirfry)
        db.session.flush()
        
        stirfry_ingredients = [
            ('chicken breast', '500g'),
            ('broccoli', '2 cups'),
            ('bell peppers', '2'),
            ('soy sauce', '3 tbsp'),
            ('garlic', '3 cloves'),
            ('ginger', '1 tbsp'),
            ('sesame oil', '1 tbsp'),
            ('rice', '2 cups cooked')
        ]
        
        for ing_name, quantity in stirfry_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=stirfry.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        stirfry.tags.extend([tags['quick'], tags['healthy']])
        
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   👥 {len(users)} users")
        print(f"   🍳 5 recipes")
        print(f"   🥘 {Ingredient.query.count()} unique ingredients")
        print(f"   🏷️  {len(tags)} tags")
        print("\n🚀 Run 'python app.py' to start the API!")

if __name__ == '__main__':
    seed_database()