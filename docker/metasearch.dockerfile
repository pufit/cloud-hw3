# syntax=docker/dockerfile:1

FROM python:latest

ARG META_INT_SEARCH_ENDPOINTS
ARG META_USERS_ENDPOINTS

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY search search
COPY tests tests

EXPOSE 8200

ENV META_INT_SEARCH_ENDPOINTS=$META_INT_SEARCH_ENDPOINTS
ENV META_USERS_ENDPOINTS=$META_USERS_ENDPOINTS

CMD ["uvicorn", "search.services.metasearch.main:app", "--host", "0.0.0.0", "--port", "8200"]
