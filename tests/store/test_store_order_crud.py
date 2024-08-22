import pytest
import requests


class TestStoreOrderCRUD:
    """Tests that CRUD-requests sent with correct data will be successfully completed."""

    def test_store_order_create(
            self, created_store_order_data, pet_id_in_order, initial_store_order_data
    ):
        assert created_store_order_data['status_code'] == 200
        assert isinstance(created_store_order_data['data']['quantity'], int) is True
        assert isinstance(created_store_order_data['data']['status'], str) is True
        assert created_store_order_data['data']['petId'] == pet_id_in_order
        assert created_store_order_data['data']['status'] == initial_store_order_data['status']

    def test_store_order_retrieve(
            self, store_order_id, store_order_id_url, initial_store_order_data
    ):
        response = requests.get(url=store_order_id_url)
        response_data = response.json()

        assert response.status_code == 200
        assert response_data['id'] == store_order_id
        assert response_data['status'] == initial_store_order_data['status']

    def test_store_order_delete(self, store_order_id_url):
        response = requests.delete(url=store_order_id_url)
        assert response.status_code == 200


class TestStoreOrderCRUDValidation:
    """Tests that CRUD-requests sent with incorrect data will result
    in 4XX errors.
    """

    def test_store_order_create_with_invalid_data(
            self, store_order_url, invalid_create_store_order_data
    ):
        response = requests.post(url=store_order_url, json=invalid_create_store_order_data)
        assert 400 <= response.status_code < 500

    def test_retrieve_non_existent_store_order(self, store_order_id_url):
        requests.delete(url=store_order_id_url)
        response = requests.get(url=store_order_id_url)

        assert response.status_code == 404
