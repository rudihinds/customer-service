from customer_service.app import create
from customer_service.infrastructure.config import Config
from customer_service.infrastructure.postgresql_customer_repository import \
    PostgreSQLCustomerRepository

if __name__ == "__main__":
    create(customer_repository=PostgreSQLCustomerRepository(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        username=Config.DB_USERNAME,
        password=Config.DB_PASSWORD,
        db=Config.DB_NAME)).run(host='0.0.0.0', port=Config.PORT)
