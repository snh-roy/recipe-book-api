from flask import Flask
from config import Config
from models import db
from routes import register_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database
    db.init_app(app)
    
    # Register routes
    register_routes(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app


if __name__ == '__main__':
    app = create_app()
    
    print("\n🚀 Recipe Book API Running!")
    print("=" * 50)
    print("Endpoints:")
    print("  Users:       POST/GET /users, GET /users/<id>")
    print("  Recipes:     POST/GET /recipes, GET/PUT/DELETE /recipes/<id>")
    print("  Ingredients: GET /ingredients, POST/DELETE /recipes/<id>/ingredients")
    print("  Tags:        GET /tags, POST /recipes/<id>/tags")
    print("  Search:      GET /recipes/search?ingredient=X&tag=Y")
    print("=" * 50)
    
    # Use environment variable for port (for deployment)
    import os
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)