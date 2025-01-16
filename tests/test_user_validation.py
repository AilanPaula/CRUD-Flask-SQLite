import pytest
import logging

logger = logging.getLogger(__name__)

    
@pytest.mark.parametrize("name,expected_error", [
    ("", "Name is required and must be between 1 and 80 characters."),
    ("A" * 81, "Name is required and must be between 1 and 80 characters."),
    (None, "Name is required and must be between 1 and 80 characters.")
])
def test_invalid_user_name(client, name, expected_error):
    """
    Função para testar se o nome é válido.
    """
    logger.info("Test invalid user name")
    response = client.post('/users', json={"name": name, "email": "ailan@example.com"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 400
    assert expected_error in response.get_json()['errors']
    
@pytest.mark.parametrize("email,expected_error", [
    ("", "Email is required and must be no longer than 50 characters."), 
    ("invalid-email", "Invalid email format."), 
    ("toolong@" + "a" * 41 + ".com", "Email must be no longer than 50 characters.")  
])
def test_invalid_user_email(client, email, expected_error):
    """
    Função para testar se o e-mail é válido.
    """
    logger.info("Test invalid user email")
    response = client.post('/users', json={"name": "Ailan Paula", "email": email})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 400
    assert expected_error in response.get_json()['errors']

         
@pytest.mark.parametrize("data,expected_error", [
    ({"name": "", "email": "ailan@example.com"}, "Name is required and must be between 1 and 80 characters."),
    ({"name": "Ailan Paula", "email": ""}, "Email is required and must be no longer than 50 characters."),
    ({}, "Name is required and must be between 1 and 80 characters.")
])
def test_create_user_missing_fields(client, data, expected_error):
    """
    Função para testar a criação do usuário com nome ou e-mail ausente.
    """
    logger.info("Test create user missing fields")
    response = client.post('/users', json=data)
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 400
    assert expected_error in response.get_json()['errors']

    
def test_update_user_optional_fields(client):
    """
    Função para testar o update com nome ou e-mail opcionais.
    """
    logger.info("Test update user optional fields")
    client.post('/users', json={"name": "Ailan Paula", "email": "ailan@example.com"})

    logger.info("Updating only the name")
    response = client.put('/users/1', json={"name": "Ailan Santos"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 200
    user = response.get_json()
    assert user['name'] == "Ailan Santos"
    assert user['email'] == "ailan@example.com"

    logger.info("Updating email only")
    response = client.put('/users/1', json={"email": "ailan.santos@example.com"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 200
    user = response.get_json()
    assert user['name'] == "Ailan Santos"
    assert user['email'] == "ailan.santos@example.com"
         
def test_email_already_exists_on_create(client):
    """
    Função para testar se o e-mail já existe no create. 
    """
    logger.info("Test email already exists on create")
    client.post('/users', json={"name": "Ailan Santos", "email": "ailan.santos@example.com"})
    response = client.post('/users', json={"name": "Ailan", "email": "ailan.santos@example.com"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 400
    assert "Email already exists" in response.get_json()['error']
    
def test_email_already_exists_on_update(client):
    """
    Função para testar se o e-mail já existe no update. 
    """
    logger.info("Test email already exists on update")
    client.post('/users', json={"name": "Ailan Paula", "email": "ailan@example.com"})
    client.post('/users', json={"name": "Paula Ailan", "email": "paula@example.com"})

    response = client.put('/users/2', json={"email": "ailan@example.com"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 400
    assert "Email already exists" in response.get_json()['error']

           
def test_not_found(client):
    """
    Função para testar se o usário existe ou não. 
    """
    logger.info("Test not found")
    response = client.get('/users/999')
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 404
    assert "User not found" in response.get_json()['error']
  
def test_conflicting_user_ids(client):
    """
    Função para testar o update em um usuário que não existe. 
    """
    logger.info("Test conflicting user ids")
    client.post('/users', json={"name": "Ailan Santos", "email": "ailan@example.com"})
    response = client.put('/users/999', json={"name": "Ailan Goncalves"})
    logger.info(f"Response status: {response.status_code}, Response JSON: {response.get_json()}")
    assert response.status_code == 404
    assert "User not found" in response.get_json()['error']



