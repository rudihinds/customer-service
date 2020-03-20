#!/bin/bash

docker build -t customer-service .;
docker run -p 5000:5000 -it customer-service;