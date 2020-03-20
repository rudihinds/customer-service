from flask import Flask

from customer_service import setup_swagger, SWAGGER_URL
from customer_service.controllers.customers import customers
from customer_service.controllers.health import health


def create(customer_repository):
    app = Flask(__name__)

    app.customer_repository = customer_repository

    app.register_blueprint(health)
    app.register_blueprint(customers)

    app.register_blueprint(setup_swagger(), url_prefix=SWAGGER_URL)

    return app
