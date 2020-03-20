import pytest

from customer_service.app import create
from customer_service.mock.mock_customer_repository import \
    MockCustomerRepository


@pytest.fixture
def web_client(app):
    return app.test_client()


@pytest.fixture
def app(customer_repository):
    return create(customer_repository=customer_repository)


@pytest.fixture()
def customer_repository():
    return MockCustomerRepository()
