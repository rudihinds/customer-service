import os


class Config:
    PORT = int(os.getenv('PORT', 5000))

    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT'))
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_NAME = os.getenv('DB_NAME')
