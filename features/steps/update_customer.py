from behave import when


@when('I update customer "{customer_id}" with surname "{surname}"')
def update_customer(context, customer_id, surname):
    context.response = context.web_client.put(
        '/customers/',
        json={'surname': surname, 'customer_id': int(customer_id)})

    assert context.response.status_code == 200, context.response.status_code
