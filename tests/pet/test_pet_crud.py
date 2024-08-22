import pytest
import requests


class TestPetCRUD:
    """Tests that CRUD-requests sent with correct data will be
    successfully completed.
    """

    def test_pet_create(self, created_pet_data, initial_pet_data):
        assert created_pet_data['status_code'] == 200
        assert isinstance(created_pet_data['data']['id'], int) is True
        assert isinstance(created_pet_data['data']['name'], str) is True
        assert created_pet_data['data']['name'] == initial_pet_data['name']
        assert created_pet_data['data']['status'] == initial_pet_data['status']

    def test_pet_update(self, pet_id, pet_url, update_pet_data):
        update_pet_data['id'] = pet_id
        response = requests.put(
            url=pet_url, json=update_pet_data
        )
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['status'] == update_pet_data['status']
        assert response_data['id'] == pet_id

    def test_pet_retrieve(self, pet_id, pet_id_url, initial_pet_data):
        response = requests.get(url=pet_id_url)
        response_data = response.json()
        assert response.status_code == 200
        assert response_data['id'] == pet_id
        assert response_data['category'] == initial_pet_data['category']
        assert response_data['name'] == initial_pet_data['name']
        assert response_data['photoUrls'] == initial_pet_data['photoUrls']
        assert response_data['tags'] == initial_pet_data['tags']
        assert response_data['status'] == initial_pet_data['status']

    def test_pet_delete(self, pet_id_url):
        response = requests.delete(url=pet_id_url)
        assert response.status_code == 200


class TestPetCRUDValidation:
    """Tests that CRUD-requests sent with incorrect data will result
    in 4XX errors.
    """

    def test_pet_create_with_invalid_data(self, pet_url, invalid_create_pet_data):
        response = requests.post(url=pet_url, json=invalid_create_pet_data)
        assert 400 <= response.status_code < 500

    def test_pet_update_with_invalid_data(self, pet_id, pet_url, invalid_update_pet_data):
        invalid_update_pet_data['id'] = pet_id
        response = requests.post(url=pet_url, json=invalid_update_pet_data)
        assert 400 <= response.status_code < 500

    def test_pet_delete_non_existent_pet(self, pet_id_url):
        response = requests.delete(url=pet_id_url)
        assert response.status_code == 200
        # try to delete just deleted object again
        response = requests.delete(url=pet_id_url)
        assert response.status_code == 404
