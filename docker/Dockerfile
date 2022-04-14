FROM python:3.8

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

EXPOSE 8000
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0

RUN apt-get update && apt-get install
RUN apt-get install -y \
  libpq-dev \
  libmariadb-dev-compat \
  libmariadb-dev \
  gcc git \
  && apt-get clean

RUN pip install -U pip

COPY ./requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt
COPY . /app/

RUN mkdir -p /app/media
RUN mkdir -p /app/staticfiles

RUN chown -R ${APP_USER}:${APP_USER} /app/media
RUN chown -R ${APP_USER}:${APP_USER} /app/staticfiles
