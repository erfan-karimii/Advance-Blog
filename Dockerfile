FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECIDE=1
ENV PTRHONUNBUFFERED=1

WORKDIR /app

COPY requirmernt.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirmernt.txt

COPY ./core /app/
