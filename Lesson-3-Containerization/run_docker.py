#/usr/bn/env/bash

#Build image
docker build --tag=api .

#list docker imagse
docker image ls

#Run flask app
docker run -p 8000:5001 api
