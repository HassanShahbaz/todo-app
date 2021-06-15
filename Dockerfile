# Dockerfile

# pull the official docker image
FROM python:3.8.3-alpine
RUN \ 
    apk update && \
    apk fix && \
    apk add --no-cache \
    bash \
    curl-dev \
    fontconfig \
    freetype-dev \
    gcc \
    gettext \
    libffi-dev \
    libjpeg-turbo-dev \
    libmagic \
    libmemcached-dev \
    libpq \
    libxml2-dev \
    libxslt-dev \
    make \
    musl-dev \
    openssl-dev \
    python3-dev \
    openssh-client \
    supervisor \
    patch \
    build-base && \
    apk add --no-cache --update-cache --repository http://nl.alpinelinux.org/alpine/v3.10/main postgresql-client=12.7-r0 postgresql-dev=12.7-r0
# set work directory
WORKDIR /todo_app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .