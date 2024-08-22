import pytest
import requests


# ----
# URLs
# ----

@pytest.fixture
def store_order_url(store_url):
    """URL for creating store order objects."""

    return f'{store_url}/order'


@pytest.fixture
def store_order_id_url(store_order_url, store_order_id):
    """URL for actions with particular store order
    objects (retrieve, delete).
    """

    return f'{store_order_url}/{store_order_id}'


# ------------------
# Valid objects data
# ------------------

@pytest.fixture
def initial_store_order_data(pet_id_in_order):
    """Data for store order creation."""

    return {
        'id': 0,
        'petId': pet_id_in_order,
        'quantity': 1,
        'shipDate': '2024-08-25T10:30:00.000Z',
        'status': 'placed',
        'complete': False
    }


@pytest.fixture
def pet_id_in_order(pet_url):
    """Sends POST-request for pet creation and returns
    created object id.
    """

    response = requests.post(
        url=pet_url, json={
            'name': 'Husky',
            'photoUrls': ['string']
        }
    )
    response_data = response.json()

    return response_data['id']


@pytest.fixture
def created_store_order_data(store_order_url, initial_store_order_data):
    """Sends POST-request for store order creation and returns created
    object data and status code.
    """

    response = requests.post(
        url=store_order_url, json=initial_store_order_data
    )
    response_status_code = response.status_code
    response_data = response.json()

    return {'status_code': response_status_code, 'data': response_data}


@pytest.fixture
def store_order_id(created_store_order_data):
    """Returns ID of a fixture store order."""

    return created_store_order_data['data']['id']


# --------------------
# Invalid objects data
# --------------------

@pytest.fixture(
    params=[
        {'quantity': 1,
         'shipDate': '2024-08-25T10:30:00.000Z',
         'status': 'placed',
         'complete': False},  # no petId field
        {'petId': 0,  # incorrect ID
         'quantity': 1,
         'shipDate': '2023-08-25T10:30:00.000Z',  # ship date from the past
         'status': 'placed',
         'complete': False},
    ]
)
def invalid_create_store_order_data(request):
    """Invalid data for store order object creating."""

    return request.param
