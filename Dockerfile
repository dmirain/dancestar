FROM ubuntu:xenial-20170119

CMD dancestar runserver 0.0.0.0:8080

RUN apt-get -qq update \
    && apt-get -qq install -y python-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install django

COPY setup.py src/
COPY dancestar/ src/dancestar/

RUN pip install /src/
