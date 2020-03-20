from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


class PostgreSQLCustomerRepository:
    def __init__(self, host, port, username, password, db):
        url = f'postgresql://{username}:{password}@{host}:{port}/{db}'
        self.engine = create_engine(url)
        declarative_base().metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def store(self, customer):
        self.session.add(customer)
        self.session.commit()

    def fetch_by_id(self, customer_id):
        try:
            return self.session \
                .query(Customer) \
                .filter(Customer.customer_id == customer_id) \
                .one()
        except NoResultFound:
            raise CustomerNotFound()
