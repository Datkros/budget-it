FROM ubuntu:bionic

RUN apt-get update -y && apt-get install -y python3-pip


COPY . /budget-it/

RUN pip3 install -r /budget-it/requirements.txt


WORKDIR /budget-it/