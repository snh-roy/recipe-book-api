from app import create_app
from models import db

app = create_app()

# Just create tables, don't seed
with app.app_context():
    db.create_all()
    print("Database tables created!")

if __name__ == "__main__":
    app.run()