# 🍳 Recipe Book API

A RESTful API for my favorite thing in the world built with Flask and SQLAlchemy. 😋

## Features

- Full CRUD operations for recipes and users
- Advanced search by ingredients and tags
- Many-to-many relationships (recipes ↔ ingredients, recipes ↔ tags)
- Comprehensive error handling and input validation
- 100% test coverage with pytest (16 unit tests)
- Seed data script with real recipes

## Tech Stack

- **Backend:** Flask, Python
- **Database:** SQLite, SQLAlchemy ORM
- **Testing:** pytest, pytest-flask
- **API Testing:** Postman

## Project Structure

```
recipe_book_api/
├── app.py                 # Application entry point
├── config.py              # Configuration settings
├── models.py              # Database models
├── seed_data.py           # Database seeding script
├── requirements.txt       # Python dependencies
├── routes/
│   ├── __init__.py
│   ├── users.py          # User endpoints
│   ├── recipes.py        # Recipe endpoints
│   ├── ingredients.py    # Ingredient endpoints
│   └── tags.py           # Tag endpoints
└── tests/
    ├── conftest.py       # Test configuration
    ├── test_users.py     # User tests
    └── test_recipes.py   # Recipe tests
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/recipe-book-api.git
   cd recipe-book-api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Seed the database:**
   ```bash
   python seed_data.py
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5001`

## API Endpoints

### Users
- `GET /users` - Get all users
- `POST /users` - Create a new user
- `GET /users/<id>` - Get a specific user

### Recipes
- `GET /recipes` - Get all recipes
- `POST /recipes` - Create a new recipe
- `GET /recipes/<id>` - Get a specific recipe with ingredients and tags
- `PUT /recipes/<id>` - Update a recipe
- `DELETE /recipes/<id>` - Delete a recipe
- `GET /recipes/search?ingredient=X&tag=Y` - Search recipes

### Ingredients
- `GET /ingredients` - Get all ingredients
- `POST /recipes/<id>/ingredients` - Add ingredient to recipe
- `DELETE /recipes/<recipe_id>/ingredients/<ingredient_id>` - Remove ingredient

### Tags
- `GET /tags` - Get all tags
- `POST /recipes/<id>/tags` - Add tag to recipe

## Example Usage

**Create a new recipe:**
```bash
curl -X POST http://localhost:5001/recipes \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Grilled Cheese",
    "instructions": "Butter bread, add cheese, grill until golden",
    "prep_time": 2,
    "cook_time": 5,
    "user_id": 1,
    "ingredients": [
      {"name": "bread", "quantity": "2 slices"},
      {"name": "cheese", "quantity": "2 slices"}
    ],
    "tags": ["quick", "comfort-food"]
  }'
```

**Search for vegetarian recipes:**
```bash
curl "http://localhost:5001/recipes/search?tag=vegetarian"
```

## Running Tests

```bash
# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

All 16 tests should pass ✅

## Database Schema

- **User** - Stores user information
- **Recipe** - Stores recipe details (linked to User)
- **Ingredient** - Stores unique ingredients
- **RecipeIngredient** - Junction table with quantities
- **Tag** - Stores recipe tags
- **recipe_tags** - Many-to-many relationship table

## Future Enhancements

- [ ] User authentication with JWT tokens
- [ ] Recipe ratings and reviews
- [ ] Image upload for recipes
- [ ] Nutritional information
- [ ] Meal planning feature
- [ ] Shopping list generator
- [ ] Pagination for large result sets

## Author

Your Name - [Sneha Roy](www.linkedin.com/in/sneharoym)


## License

This project is open source and available under the MIT License.