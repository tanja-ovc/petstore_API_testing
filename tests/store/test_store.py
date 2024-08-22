import requests


class TestStore:
    """Tests store related functionality."""

    def test_store_inventory_retrieve(self, store_inventory_url):
        response = requests.get(url=store_inventory_url)
        response_data = response.json()

        assert response.status_code == 200
        assert all(isinstance(value, int) for value in response_data.values())
