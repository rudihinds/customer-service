import pytest

from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_fetch_by_id_raise_when_not_found(customer_repository):
    with pytest.raises(CustomerNotFound):
        customer_repository.fetch_by_id(87654)


def test_store_stores_customer_with_id(customer_repository):
    nicole = Customer(customer_id=123, first_name="Nicole", surname="Forsgren")
    jez = Customer(customer_id=321, first_name="Jez", surname="Humble")
    customer_repository.store(nicole)
    customer_repository.store(jez)
    assert customer_repository.fetch_by_id(123) is nicole
    assert customer_repository.fetch_by_id(321) is jez


def test_store_new_customer(customer_repository):
    nicole = Customer(first_name="Nicole", surname="Forsgren")
    jez = Customer(first_name="Jez", surname="Humble")
    customer_repository.store(nicole)
    customer_repository.store(jez)
    assert customer_repository.fetch_by_id(nicole.customer_id) is nicole
    assert customer_repository.fetch_by_id(jez.customer_id) is jez
