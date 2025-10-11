import pytest
from app import create_app
from models import db, User

class TestConfig:
    """Test configuration - uses in-memory database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-secret-key'

@pytest.fixture(scope='function')
def app():
    """Create application for testing"""
    app = create_app(TestConfig)
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Test client for making requests"""
    return app.test_client()

@pytest.fixture
def sample_user(app):
    """Create a sample user for tests"""
    with app.app_context():
        user = User(name="Test User", email="test@example.com")
        db.session.add(user)
        db.session.commit()
        # Return the ID, not the object
        user_id = user.id
    return user_id