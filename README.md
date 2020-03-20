# Customer Service

Returns the details of just one customer - Joe Bloggs

## Installation

```
pip install pipenv
pipenv install --dev
```

### To run tests

```
pipenv run python -m pytest
```

### To run the service

```
FLASK_APP=customer_service pipenv run flask run
```

### Commands

```
docker build -t customer-service .
docker run -p 8080:8080 -it customer-service
```
