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
            User(name="International Chef", email="chef@world.com"),
            User(name="Home Cook", email="homecook@recipes.com"),
            User(name="Food Explorer", email="explorer@cuisine.com")
        ]
        db.session.add_all(users)
        db.session.commit()
        
        # Create tags
        print("🏷️  Creating tags...")
        tags_data = ['albanian', 'american', 'italian', 'french', 'chinese', 'british', 'indian', 'japanese', 'comfort-food', 'traditional', 'quick', 'spicy']
        tags = {name: Tag(name=name) for name in tags_data}
        db.session.add_all(tags.values())
        db.session.commit()
        
        # Create international recipes
        print("🍳 Creating international recipes...")
        
        # Recipe 1: Albanian - Tavë Kosi
        tave_kosi = Recipe(
            name="Tavë Kosi (Albanian Baked Lamb with Yogurt)",
            instructions="1. Season lamb chunks with salt and pepper. 2. Brown lamb in butter. 3. Add flour and water, simmer until tender (45 min). 4. Mix yogurt with eggs and flour. 5. Pour lamb into baking dish. 6. Cover with yogurt mixture. 7. Bake at 350°F for 30 minutes until golden.",
            prep_time=20,
            cook_time=75,
            user_id=users[0].id
        )
        db.session.add(tave_kosi)
        db.session.flush()
        
        tave_kosi_ingredients = [
            ('lamb chunks', '1kg'),
            ('greek yogurt', '500g'),
            ('eggs', '4'),
            ('flour', '3 tbsp'),
            ('butter', '3 tbsp'),
            ('rice', '1 cup cooked'),
            ('salt', '2 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in tave_kosi_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=tave_kosi.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        tave_kosi.tags.extend([tags['albanian'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 2: American - Classic Burger
        burger = Recipe(
            name="Classic American Cheeseburger",
            instructions="1. Form ground beef into patties, season with salt and pepper. 2. Grill on high heat 4 minutes per side. 3. Add cheese slice in last minute. 4. Toast burger buns. 5. Assemble: bun bottom, lettuce, tomato, patty with cheese, onion, pickles, ketchup, mustard, top bun.",
            prep_time=10,
            cook_time=10,
            user_id=users[1].id
        )
        db.session.add(burger)
        db.session.flush()
        
        burger_ingredients = [
            ('ground beef', '600g'),
            ('cheddar cheese', '4 slices'),
            ('burger buns', '4'),
            ('lettuce', '4 leaves'),
            ('tomato', '1 large'),
            ('onion', '1'),
            ('pickles', '8 slices'),
            ('ketchup', '4 tbsp'),
            ('mustard', '2 tbsp'),
            ('salt', '1 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in burger_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=burger.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        burger.tags.extend([tags['american'], tags['quick'], tags['comfort-food']])
        
        # Recipe 3: Italian - Pasta Carbonara
        carbonara = Recipe(
            name="Spaghetti alla Carbonara",
            instructions="1. Cook spaghetti in salted boiling water. 2. Fry guanciale until crispy. 3. Beat eggs with pecorino romano. 4. Drain pasta, reserve 1 cup pasta water. 5. Toss hot pasta with guanciale. 6. Remove from heat, add egg mixture, toss quickly. 7. Add pasta water to create creamy sauce. 8. Season with black pepper.",
            prep_time=10,
            cook_time=15,
            user_id=users[0].id
        )
        db.session.add(carbonara)
        db.session.flush()
        
        carbonara_ingredients = [
            ('spaghetti', '400g'),
            ('guanciale', '200g'),
            ('eggs', '4'),
            ('pecorino romano cheese', '100g'),
            ('black pepper', '2 tsp'),
            ('salt', '1 tsp')
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
        
        carbonara.tags.extend([tags['italian'], tags['traditional'], tags['quick']])
        
        # Recipe 4: French - Coq au Vin
        coq_au_vin = Recipe(
            name="Coq au Vin (Chicken in Wine)",
            instructions="1. Brown chicken pieces in butter. 2. Sauté bacon, mushrooms, and pearl onions. 3. Flambe with cognac. 4. Add red wine, chicken stock, thyme, bay leaf. 5. Return chicken to pot. 6. Simmer covered for 1 hour. 7. Thicken sauce with butter and flour. 8. Garnish with parsley.",
            prep_time=30,
            cook_time=90,
            user_id=users[2].id
        )
        db.session.add(coq_au_vin)
        db.session.flush()
        
        coq_ingredients = [
            ('chicken thighs', '8 pieces'),
            ('red wine', '2 cups'),
            ('bacon', '150g'),
            ('mushrooms', '300g'),
            ('pearl onions', '200g'),
            ('chicken stock', '1 cup'),
            ('cognac', '3 tbsp'),
            ('butter', '4 tbsp'),
            ('flour', '2 tbsp'),
            ('thyme', '3 sprigs'),
            ('bay leaf', '2'),
            ('parsley', '1/4 cup'),
            ('salt', '1 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in coq_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=coq_au_vin.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        coq_au_vin.tags.extend([tags['french'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 5: Chinese - Kung Pao Chicken
        kung_pao = Recipe(
            name="Kung Pao Chicken",
            instructions="1. Marinate diced chicken in soy sauce and cornstarch. 2. Mix sauce: soy sauce, vinegar, sugar, sesame oil. 3. Stir-fry chicken in hot wok with oil. 4. Add dried chilies and Sichuan peppercorns. 5. Add bell peppers, garlic, ginger. 6. Pour in sauce. 7. Add roasted peanuts. 8. Serve over rice.",
            prep_time=20,
            cook_time=10,
            user_id=users[1].id
        )
        db.session.add(kung_pao)
        db.session.flush()
        
        kung_pao_ingredients = [
            ('chicken breast', '500g'),
            ('roasted peanuts', '1 cup'),
            ('dried red chilies', '8'),
            ('sichuan peppercorns', '1 tsp'),
            ('bell peppers', '2'),
            ('soy sauce', '4 tbsp'),
            ('rice vinegar', '2 tbsp'),
            ('sugar', '2 tbsp'),
            ('sesame oil', '1 tbsp'),
            ('cornstarch', '2 tbsp'),
            ('garlic', '4 cloves'),
            ('ginger', '2 tbsp minced'),
            ('vegetable oil', '3 tbsp'),
            ('green onions', '3')
        ]
        
        for ing_name, quantity in kung_pao_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=kung_pao.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        kung_pao.tags.extend([tags['chinese'], tags['spicy'], tags['quick']])
        
        # Recipe 6: British - Fish and Chips
        fish_chips = Recipe(
            name="Classic Fish and Chips",
            instructions="1. Cut potatoes into thick chips, soak in water. 2. Make batter: flour, baking powder, beer, salt. 3. Dry fish fillets, season with salt. 4. Heat oil to 350°F. 5. Fry chips until golden, drain. 6. Dip fish in batter, fry until crispy. 7. Fry chips again for extra crunch. 8. Serve with malt vinegar and mushy peas.",
            prep_time=30,
            cook_time=20,
            user_id=users[0].id
        )
        db.session.add(fish_chips)
        db.session.flush()
        
        fish_chips_ingredients = [
            ('cod fillets', '4 large'),
            ('potatoes', '1kg'),
            ('flour', '2 cups'),
            ('baking powder', '2 tsp'),
            ('beer', '1 cup'),
            ('vegetable oil', '2 liters for frying'),
            ('malt vinegar', '1/4 cup'),
            ('salt', '2 tsp'),
            ('lemon', '1')
        ]
        
        for ing_name, quantity in fish_chips_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=fish_chips.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        fish_chips.tags.extend([tags['british'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 7: Indian - Butter Chicken
        butter_chicken = Recipe(
            name="Butter Chicken (Murgh Makhani)",
            instructions="1. Marinate chicken in yogurt, garam masala, turmeric for 2 hours. 2. Grill or pan-fry chicken. 3. Sauté onion, garlic, ginger in butter. 4. Add tomato puree, cook 10 minutes. 5. Add cream, garam masala, fenugreek. 6. Add cooked chicken. 7. Simmer 15 minutes. 8. Garnish with cream and cilantro. Serve with naan.",
            prep_time=130,
            cook_time=30,
            user_id=users[2].id
        )
        db.session.add(butter_chicken)
        db.session.flush()
        
        butter_chicken_ingredients = [
            ('chicken thighs', '750g'),
            ('greek yogurt', '1 cup'),
            ('heavy cream', '1 cup'),
            ('butter', '6 tbsp'),
            ('tomato puree', '2 cups'),
            ('onion', '1 large'),
            ('garlic', '6 cloves'),
            ('ginger', '3 tbsp minced'),
            ('garam masala', '2 tbsp'),
            ('turmeric', '1 tsp'),
            ('kasuri methi', '1 tbsp'),
            ('cilantro', '1/4 cup'),
            ('salt', '2 tsp')
        ]
        
        for ing_name, quantity in butter_chicken_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=butter_chicken.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        butter_chicken.tags.extend([tags['indian'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 8: Japanese - Tonkotsu Ramen
        ramen = Recipe(
            name="Tonkotsu Ramen",
            instructions="1. Boil pork bones for 12+ hours to make milky broth. 2. Marinate soft-boiled eggs in soy sauce mixture. 3. Cook ramen noodles according to package. 4. Slice chashu pork. 5. Assemble: hot broth in bowl, add noodles. 6. Top with chashu, egg halves, nori, green onions, bamboo shoots. 7. Add sesame seeds and chili oil.",
            prep_time=60,
            cook_time=720,
            user_id=users[1].id
        )
        db.session.add(ramen)
        db.session.flush()
        
        ramen_ingredients = [
            ('pork bones', '2kg'),
            ('pork belly', '500g'),
            ('ramen noodles', '4 servings'),
            ('eggs', '4'),
            ('soy sauce', '1 cup'),
            ('mirin', '1/2 cup'),
            ('green onions', '6'),
            ('nori seaweed', '4 sheets'),
            ('bamboo shoots', '200g'),
            ('sesame seeds', '2 tbsp'),
            ('chili oil', '2 tbsp'),
            ('garlic', '8 cloves'),
            ('ginger', '4 slices')
        ]
        
        for ing_name, quantity in ramen_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=ramen.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        ramen.tags.extend([tags['japanese'], tags['traditional'], tags['comfort-food']])
        
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   👥 {len(users)} users")
        print(f"   🍳 8 international recipes")
        print(f"   🥘 {Ingredient.query.count()} unique ingredients")
        print(f"   🏷️  {len(tags)} tags")

if __name__ == '__main__':
    seed_database()
        
        # Recipe 1: Ćevapi
        cevapi = Recipe(
            name="Ćevapi (Balkan Grilled Sausages)",
            instructions="1. Mix ground beef and lamb with minced garlic, salt, pepper, and paprika. 2. Form into small finger-shaped sausages. 3. Refrigerate for 2 hours. 4. Grill on high heat for 8-10 minutes, turning frequently. 5. Serve in lepinja bread with raw onions and ajvar.",
            prep_time=30,
            cook_time=10,
            user_id=users[0].id
        )
        db.session.add(cevapi)
        db.session.flush()
        
        cevapi_ingredients = [
            ('ground beef', '500g'),
            ('ground lamb', '250g'),
            ('garlic', '4 cloves'),
            ('paprika', '2 tsp'),
            ('salt', '1 tsp'),
            ('black pepper', '1 tsp'),
            ('onion', '2 large'),
            ('lepinja bread', '4 pieces')
        ]
        
        for ing_name, quantity in cevapi_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=cevapi.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        cevapi.tags.extend([tags['balkan'], tags['traditional'], tags['meat-lovers']])
        
        # Recipe 2: Burek
        burek = Recipe(
            name="Burek (Flaky Meat Pie)",
            instructions="1. Brown ground beef with onions. 2. Season with salt and pepper. 3. Layer phyllo dough in greased pan, brushing each layer with oil. 4. Add meat filling. 5. Continue layering phyllo on top. 6. Score into squares. 7. Bake at 375°F for 35-40 minutes until golden.",
            prep_time=45,
            cook_time=40,
            user_id=users[1].id
        )
        db.session.add(burek)
        db.session.flush()
        
        burek_ingredients = [
            ('phyllo dough', '1 package'),
            ('ground beef', '750g'),
            ('onion', '2 large'),
            ('vegetable oil', '1 cup'),
            ('salt', '2 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in burek_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=burek.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        burek.tags.extend([tags['balkan'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 3: Shopska Salad
        shopska = Recipe(
            name="Shopska Salata (Bulgarian Salad)",
            instructions="1. Dice tomatoes, cucumbers, and peppers into medium chunks. 2. Dice onion finely. 3. Mix vegetables in bowl. 4. Season with salt, oil, and vinegar. 5. Top generously with grated sirene (feta) cheese. 6. Garnish with parsley. 7. Serve immediately.",
            prep_time=15,
            cook_time=0,
            user_id=users[2].id
        )
        db.session.add(shopska)
        db.session.flush()
        
        shopska_ingredients = [
            ('tomatoes', '4 large'),
            ('cucumber', '2'),
            ('green bell pepper', '2'),
            ('onion', '1'),
            ('feta cheese', '200g'),
            ('olive oil', '3 tbsp'),
            ('white vinegar', '2 tbsp'),
            ('parsley', '1/4 cup'),
            ('salt', 'to taste')
        ]
        
        for ing_name, quantity in shopska_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=shopska.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        shopska.tags.extend([tags['balkan'], tags['vegetarian'], tags['traditional']])
        
        # Recipe 4: Sarma
        sarma = Recipe(
            name="Sarma (Stuffed Cabbage Rolls)",
            instructions="1. Blanch cabbage leaves in boiling water. 2. Mix ground pork, rice, onion, and spices. 3. Place filling on each leaf and roll tightly. 4. Layer rolls in pot with sauerkraut. 5. Add water to cover. 6. Simmer on low heat for 2 hours. 7. Serve with sour cream.",
            prep_time=60,
            cook_time=120,
            user_id=users[0].id
        )
        db.session.add(sarma)
        db.session.flush()
        
        sarma_ingredients = [
            ('cabbage', '1 large head'),
            ('ground pork', '1kg'),
            ('rice', '1 cup'),
            ('onion', '2'),
            ('paprika', '2 tbsp'),
            ('sauerkraut', '500g'),
            ('tomato paste', '3 tbsp'),
            ('sour cream', '1 cup'),
            ('salt', '2 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in sarma_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=sarma.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        sarma.tags.extend([tags['balkan'], tags['traditional'], tags['comfort-food']])
        
        # Recipe 5: Palacinke
        palacinke = Recipe(
            name="Palačinke (Balkan Crepes)",
            instructions="1. Whisk eggs, flour, milk, and salt until smooth. 2. Let batter rest 30 minutes. 3. Heat lightly oiled pan. 4. Pour thin layer of batter, swirl to coat pan. 5. Cook until golden, flip. 6. Fill with Nutella, jam, or nuts. 7. Roll or fold and dust with powdered sugar.",
            prep_time=40,
            cook_time=20,
            user_id=users[2].id
        )
        db.session.add(palacinke)
        db.session.flush()
        
        palacinke_ingredients = [
            ('flour', '2 cups'),
            ('eggs', '3'),
            ('milk', '2 cups'),
            ('salt', 'pinch'),
            ('butter', '2 tbsp'),
            ('nutella', '1 cup'),
            ('powdered sugar', '1/4 cup'),
            ('walnuts', '1/2 cup chopped')
        ]
        
        for ing_name, quantity in palacinke_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=palacinke.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        palacinke.tags.extend([tags['balkan'], tags['dessert'], tags['breakfast']])
        
        # Recipe 6: Ajvar
        ajvar = Recipe(
            name="Ajvar (Roasted Red Pepper Spread)",
            instructions="1. Roast red peppers and eggplant until charred. 2. Peel skins off vegetables. 3. Remove seeds from peppers. 4. Finely chop or blend vegetables. 5. Cook in oil with garlic for 1 hour, stirring frequently. 6. Season with salt and vinegar. 7. Store in sterilized jars.",
            prep_time=90,
            cook_time=60,
            user_id=users[1].id
        )
        db.session.add(ajvar)
        db.session.flush()
        
        ajvar_ingredients = [
            ('red bell peppers', '3kg'),
            ('eggplant', '1kg'),
            ('garlic', '6 cloves'),
            ('sunflower oil', '1 cup'),
            ('white vinegar', '2 tbsp'),
            ('salt', '2 tsp'),
            ('black pepper', '1 tsp')
        ]
        
        for ing_name, quantity in ajvar_ingredients:
            ingredient = Ingredient.query.filter_by(name=ing_name).first()
            if not ingredient:
                ingredient = Ingredient(name=ing_name)
                db.session.add(ingredient)
                db.session.flush()
            
            recipe_ing = RecipeIngredient(
                recipe_id=ajvar.id,
                ingredient_id=ingredient.id,
                quantity=quantity
            )
            db.session.add(recipe_ing)
        
        ajvar.tags.extend([tags['balkan'], tags['traditional'], tags['vegetarian']])
        
        db.session.commit()
        
        print("✅ Database seeded successfully!")
        print(f"   👥 {len(users)} users")
        print(f"   🍳 6 Balkan recipes")
        print(f"   🥘 {Ingredient.query.count()} unique ingredients")
        print(f"   🏷️  {len(tags)} tags")

if __name__ == '__main__':
    seed_database()