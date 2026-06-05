import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_terms(client):
    rv = client.get('/api/terms')
    assert rv.status_code == 200
    data = rv.get_json()
    assert len(data) == 20

def test_get_single_term(client):
    rv = client.get('/api/terms?modality=acoustic&harmType=harassment')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['modality'] == 'acoustic'
    assert data['harmType'] == 'harassment'
