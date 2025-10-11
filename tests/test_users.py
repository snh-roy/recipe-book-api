import pytest
import json

class TestUsers:
    def test_create_user(self, client):
        """Test creating a new user"""
        response = client.post('/users', 
            data=json.dumps({'name': 'Bob Smith', 'email': 'bob@example.com'}),
            content_type='application/json'
        )
        
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == 'Bob Smith'
        assert data['email'] == 'bob@example.com'
        assert 'id' in data
    
    def test_create_user_duplicate_email(self, client, sample_user):
        """Test that duplicate emails are rejected"""
        response = client.post('/users',
            data=json.dumps({'name': 'Alice Clone', 'email': 'test@example.com'}),
            content_type='application/json'
        )
        
        # This will actually fail right now! You need to add error handling
        # Expected: 400 or 409 status code
        assert response.status_code in [400, 409]
    
    def test_get_all_users(self, client, sample_user):
        """Test retrieving all users"""
        response = client.get('/users')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) >= 1
        assert data[0]['email'] == 'test@example.com'
    
    def test_get_user_by_id(self, client, sample_user):
        """Test retrieving a specific user"""
        response = client.get(f'/users/{sample_user}')
        
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['name'] == 'Test User'
    
    def test_get_nonexistent_user(self, client):
        """Test retrieving a user that doesn't exist"""
        response = client.get('/users/999')
        
        assert response.status_code == 404
    
    def test_create_user_missing_fields(self, client):
        """Test creating user with missing required fields"""
        response = client.post('/users',
            data=json.dumps({'name': 'Incomplete User'}),
            content_type='application/json'
        )
        
        # This will fail too! Need validation
        # Expected: 400 status code
        assert response.status_code == 400