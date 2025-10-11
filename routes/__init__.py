from flask import Blueprint

def register_routes(app):
    from .users import users_bp
    from .recipes import recipes_bp
    from .ingredients import ingredients_bp
    from .tags import tags_bp
    
    app.register_blueprint(users_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(tags_bp)