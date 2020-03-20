import os

from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load

SWAGGER_URL = '/docs'


def setup_swagger():
    swagger_yml = load(open(get_app_base_path() + '/../swagger.yml', 'r'),
                       Loader=Loader)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        '',
        config={  # Swagger UI config overrides
            'app_name': "Customer Service API",
            'spec': swagger_yml
        },
    )

    return swaggerui_blueprint


def get_app_base_path():
    return os.path.dirname(os.path.realpath(__file__))
