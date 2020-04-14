import pytest

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_customer_when_customer_does_not_exist(customer_repository):
    with pytest.raises(CustomerNotFound):
        commands.get_customer(customer_id=99999,
                              customer_repository=customer_repository)


def test_get_customer(customer_repository):
    customer = Customer(customer_id=1234, first_name='Gene', surname='Kim')
    customer_repository.store(customer)

    result = commands.get_customer(customer_id=1234,
                                   customer_repository=customer_repository)

    assert result is customer


def test_create_customer(customer_repository):
    id = commands.create_customer(first_name='Nicole',
                                  surname='Forsgren',
                                  customer_repository=customer_repository)

    stored_customer = customer_repository.fetch_by_id(id)

    assert stored_customer.first_name == 'Nicole'
    assert stored_customer.surname == 'Forsgren'


def test_update_customer(customer_repository):
    customer1 = Customer(
        customer_id=123456,
        first_name='Rudi',
        surname='Joyel')
    customer2 = Customer(
        customer_id=12345,
        first_name='Nicole',
        surname='Forsgren')
    customer_repository.store(customer1)
    customer_repository.store(customer2)

    commands.update_customer(customer_id=123456, surname="Jack",
                             customer_repository=customer_repository)

    commands.update_customer(customer_id=12345, surname="Woods",
                             customer_repository=customer_repository)

    updated_customer1 = customer_repository.fetch_by_id(123456)
    updated_customer2 = customer_repository.fetch_by_id(12345)

    assert updated_customer1.first_name == "Rudi"
    assert updated_customer1.surname == "Jack"

    assert updated_customer2.first_name == "Nicole"
    assert updated_customer2.surname == "Woods"
