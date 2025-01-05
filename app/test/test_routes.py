import pytest
from app.routes import app
from flask import session

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    app.secret_key = "testsecret"
    with app.test_client() as client:
        with client.session_transaction() as sess:
            sess.clear()  # Clear any existing session data for a fresh start
        yield client


def test_index(client):
    """Test the home page before starting the game."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Start Game" in response.data


def test_start_game(client):
    """Test starting a new game."""
    response = client.get('/start')
    assert response.status_code == 302  # Redirect to '/'
    with client.session_transaction() as sess:
        assert 'target_word' in sess  # Ensure the session has the target word
        assert sess['attempts'] == []  # Ensure attempts are cleared
