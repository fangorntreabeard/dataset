FROM python:3.10.6

# рабочая директория
#WORKDIR /usr/src/app

# переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt

# установка зависимостей
RUN set -eux \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app/