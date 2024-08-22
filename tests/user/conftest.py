import pytest
import requests


# ----
# URLs
# ----

@pytest.fixture(scope='package')
def user_url(base_url):
    """General user URL."""

    return f'{base_url}/user'


@pytest.fixture(scope='package')
def user_create_with_list_url(user_url):
    """Users creation URL."""

    return f'{user_url}/createWithList'


# ------------------
# Valid objects data
# ------------------

@pytest.fixture
def initial_user_data():
    """Data for users creation."""

    return [{
        'id': 0,
        'username': 'user_arbuzer',
        'firstName': 'First Name',
        'lastName': 'Last Name',
        'email': 'email@mail.com',
        'password': 'password',
        'phone': '89990007766',
        'userStatus': 0,
    }]


@pytest.fixture
def created_user_data(user_url, user_create_with_list_url, initial_user_data):
    """Sends POST-request for user creation and returns created
    username and password.
    """

    requests.post(
        url=user_create_with_list_url, json=initial_user_data
    )

    response = requests.get(
        f'{user_url}/{initial_user_data[0]['username']}'
    )
    response_data = response.json()

    return response_data['username'], response_data['password']


# --------------------
# Invalid objects data
# --------------------

@pytest.fixture(
    params=[
        [{
            'id': 0,
            'username': 'user_invalid_arbuzer',
            'firstName': 'First Invalid Name',
            'lastName': 'Last Invalid Name',
            'email': 'invalid@mail.com',
            'phone': '00000000000',
            'userStatus': 0,
        }],  # no password provided
        [{
            'email': 'emailllllllll',  # incorrect email format; not enough fields
        }],
    ]
)
def invalid_create_user_data(request):
    """Invalid data for user object creating."""

    return request.param
