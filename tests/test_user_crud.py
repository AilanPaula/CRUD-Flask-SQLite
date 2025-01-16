import pytest
import logging

logger = logging.getLogger(__name__)

def test_add_user(client):
    """
    Função para testar se um usuário pode ser adicionado corretamente. 
    """
    logger.info("Test add user")
    payload = {"name": "Ailan Paula", "email": "ailan@example.com"}
    response = client.post('/users', json=payload)
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 201
    assert response.get_json()['name'] == "Ailan Paula"
    assert response.get_json()['email'] == "ailan@example.com"
    
def test_get_users(client):
    """
    Função para testar se os usuários cadastrados são listados.
    """
    logger.info("Test get users")
    payload = {"name": "Ailan Paula", "email": "ailan@example.com"}
    client.post('/users', json=payload)
    response = client.get('/users')
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 200

def test_update_user(client):
    """
    Função para testar se um usuário pode ser atualizado. 
    """
    logger.info("Test update user")
    payload = {"name": "Ailan Paula", "email": "ailan@example.com"}
    client.post('/users', json=payload)
    response = client.put('/users/1', json={"name": "Ailan Paula"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 200
    assert "Ailan Paula" in response.get_json()['name']

def test_delete_user(client):
    """
    Função para testar se um usuário pode ser deletado.
    """
    logger.info("Test delete user")
    payload = {"name": "Ailan Paula", "email": "ailan@example.com"}
    client.post('/users', json=payload)
    response = client.delete('/users/1')
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 200
    assert 'User deleted' in response.get_json()['message']
    
