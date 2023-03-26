FROM python:3.10.7-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /project
COPY . /project
RUN pip install --no-cache-dir -r requirements_local.txt