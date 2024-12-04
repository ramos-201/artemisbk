import pytest
from starlette.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_register_user_mutation(client):
    mutation = '''
    mutation(
        $name: String!,
        $lastName: String!,
        $user: String!,
        $email: String!,
        $mobilePhone: String!,
        $password: String!
    ) {
        registerUser(
            name: $name,
            lastName: $lastName,
            user: $user,
            email: $email,
            mobilePhone: $mobilePhone,
            password: $password
        ) {
            data
            response
        }
    }
    '''
    variables = {
        'name': 'john',
        'lastName': 'smith',
        'user': 'john.smith',
        'email': 'john.smith@example.com',
        'mobilePhone': '3171111111',
        'password': 'password_example',
    }

    response = client.post('/graphql', json={'query': mutation, 'variables': variables})
    assert response.status_code == 200

    data = response.json()
    assert data == 'john'
