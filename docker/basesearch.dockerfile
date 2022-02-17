# syntax=docker/dockerfile:1

FROM python:latest

ARG BASE_SEARCH_DATA_PATH
ARG PORT=8000

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY search search
COPY data data

EXPOSE $PORT

ENV BASE_SEARCH_DATA_PATH=$BASE_SEARCH_DATA_PATH

ENV PORT=$PORT
CMD uvicorn search.services.basesearch.main:app --host 0.0.0.0 --port ${PORT}
