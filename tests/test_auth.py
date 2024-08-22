import requests


def test_authentication(store_inventory_url):
    auth_response = requests.get(store_inventory_url, headers={
        'Authorization': 'special-key',
    })
    unauth_response = requests.get(store_inventory_url)

    assert auth_response.status_code == 200
    assert 400 <= unauth_response.status_code <= 403
