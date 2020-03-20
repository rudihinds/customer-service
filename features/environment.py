from customer_service import app
from customer_service.mock.mock_customer_repository import \
    MockCustomerRepository


def before_all(context):
    context.customer_repository = MockCustomerRepository()
    context.web_client = app.create(
        customer_repository=context.customer_repository).test_client()
