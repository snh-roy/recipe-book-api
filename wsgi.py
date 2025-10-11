from app import create_app
from models import db, User
import os

app = create_app()

# Seed database on first startup if empty
with app.app_context():
    try:
        db.create_all()
        if User.query.count() == 0:
            print("Database is empty, running seed...")
            # Import renamed module
            import _seed_data
            _seed_data.seed_database()
            print("Seed complete!")
    except Exception as e:
        print(f"Database setup: {e}")

if __name__ == "__main__":
    app.run()