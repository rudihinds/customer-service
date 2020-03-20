from unittest.mock import patch

import pytest

from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


@patch('customer_service.model.commands.get_customer')
def test_get_customer_id(get_customer, web_client, customer_repository):
    get_customer.return_value = Customer(customer_id=12345,
                                         first_name='Joe',
                                         surname='Bloggs')

    response = web_client.get('/customers/12345')

    get_customer.assert_called_with(
        customer_id=12345,
        customer_repository=customer_repository)
    assert response.is_json
    assert response.get_json() == dict(customerId='12345',
                                       firstName='Joe',
                                       surname='Bloggs')


@patch('customer_service.model.commands.get_customer')
def test_get_customer_not_found(get_customer, web_client):
    get_customer.side_effect = CustomerNotFound()

    response = web_client.get('/customers/000000')

    assert response.is_json
    assert response.status_code == 404
    assert response.get_json() == dict(message='Customer not found')


@patch('customer_service.model.commands.create_customer')
def test_create_customer(create_customer, web_client, customer_repository):
    create_customer.return_value = '98765'

    request_body = dict(firstName='Jez', surname='Humble')

    response = web_client.post('/customers/', json=request_body)

    assert response.status_code == 201

    create_customer.assert_called_with(
        first_name='Jez',
        surname='Humble',
        customer_repository=customer_repository)

    assert response.is_json

    account = response.get_json()

    assert account == dict(
        firstName='Jez',
        surname='Humble',
        customerId='98765')


@pytest.mark.parametrize(
    'bad_payload',
    [dict(),
     dict(firstName='Joe', surname='Bloggs', unknown='value'),
     dict(firstName='', surname='Bloggs'),
     dict(firstName='Joe', surname='')])
def test_create_customer_with_bad_payload(web_client, bad_payload):
    response = web_client.post('/customers/', json=bad_payload)
    assert response.status_code == 400


def test_create_customer_with_bad_context_type(web_client):
    response = web_client.post('/customers/', data='not json')
    assert response.status_code == 415
    assert response.get_json()['message'] == 'Request must be application/json'
