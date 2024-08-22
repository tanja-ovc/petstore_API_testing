import pytest
import requests


class TestPetActions:
    """Tests functionality other than CRUD operations."""

    @pytest.mark.parametrize(
        'status_in_url, status_result', [
            ('available', {'available'}),
            ('pending', {'pending'}),
            ('sold', {'sold'}),
            ('wrong_status', set())
        ]
    )
    def test_pet_get_by_status(
            self, pet_url, status_in_url, status_result, initial_pet_data
    ):
        # make sure we'll have pet objects with "available", "pending"
        # and "sold" statuses
        requests.post(url=pet_url, json=initial_pet_data)
        initial_pet_data['status'] = 'sold'
        requests.post(url=pet_url, json=initial_pet_data)
        initial_pet_data['status'] = 'pending'
        requests.post(url=pet_url, json=initial_pet_data)

        url_status_filter = f'{pet_url}/findByStatus?status={status_in_url}'

        response = requests.get(url=url_status_filter)
        response_data = response.json()

        status = set([pet['status'] for pet in response_data])

        assert response.status_code == 200
        assert status == status_result

    def test_update_pet_with_form_data(self, pet_id, pet_id_url):
        response = requests.post(
            url=pet_id_url,
            data={'id': pet_id, 'name': 'Lessie', 'status': 'sold'}
        )

        assert response.status_code == 200

        response = requests.get(url=pet_id_url)
        response_data = response.json()

        assert response_data['name'] == 'Lessie'
        assert response_data['status'] == 'sold'
        assert response_data['id'] == pet_id
