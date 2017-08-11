FROM python:2.7

RUN apt-get update && apt-get install -y wget
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-amd64-v0.2.0.tar.gz
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install ipython
RUN pip install pytest>=3.2.0
RUN pip install mock>=2.0.0
RUN pip install kombu>=4.1.0

COPY . /usr/src/app

