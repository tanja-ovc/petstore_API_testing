import pytest
import requests


# ----
# URLs
# ----

@pytest.fixture
def pet_id_url(base_url, pet_id):
    """URL for actions with particular pet objects
    (retrieve, update, delete...).
    """

    return f'{base_url}/pet/{pet_id}'


# ------------------
# Valid objects data
# ------------------

@pytest.fixture(scope='class')
def initial_pet_data():
    """Data for pet object creation."""

    return {
        'id': 0,
        'category': {'id': 0, 'name': 'string'},
        'name': 'Buba',
        'photoUrls': ['string'],
        'tags': [{'id': 0, 'name': 'string'}],
        'status': 'available'
    }


@pytest.fixture
def created_pet_data(pet_url, initial_pet_data):
    """Sends POST-request for pet creation and returns created
    object data and status code.
    """

    response = requests.post(
        url=pet_url, json=initial_pet_data
    )
    response_status_code = response.status_code
    response_data = response.json()

    return {'status_code': response_status_code, 'data': response_data}


@pytest.fixture
def pet_id(created_pet_data):
    """Returns ID of a fixture pet."""

    return created_pet_data['data']['id']


@pytest.fixture
def update_pet_data():
    """Data for pet object updating."""

    return {'status': 'sold'}


# --------------------
# Invalid objects data
# --------------------

@pytest.fixture(
    params=[
        {'name': list()},  # invalid data type
        {'name': 'Bobby',
         'photoUrls': ['string'],
         'status': 'non-existent status'},  # invalid status - should be"available"/"pending"/"sold"
    ]
)
def invalid_update_pet_data(request):
    """Invalid data for pet object updating."""

    return request.param


@pytest.fixture(
    params=[
        {'name': 'Jackie'},  # no required field 'photoUrls'
        {'photoUrls': ['string']},  # no required field 'name'
    ]
)
def invalid_create_pet_data(request):
    """Invalid data for pet object creating."""

    return request.param
