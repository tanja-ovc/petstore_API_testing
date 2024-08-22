import pytest


@pytest.fixture(scope='session')
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture(scope='session')
def pet_url(base_url):
    """URL for creating and updating pet objects."""

    return f'{base_url}/pet'


@pytest.fixture(scope='session')
def store_url(base_url):
    """General store URL."""

    return f'{base_url}/store'


@pytest.fixture(scope='session')
def store_inventory_url(store_url):
    """Store inventory URL."""

    return f'{store_url}/inventory'
