# syntax=docker/dockerfile:1

FROM python:latest

ARG INT_BASE_SEARCH_ENDPOINTS

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY search search

EXPOSE 8100

ENV INT_BASE_SEARCH_ENDPOINTS=$INT_BASE_SEARCH_ENDPOINTS

CMD ["uvicorn", "search.services.intsearch.main:app", "--host", "0.0.0.0", "--port", "8100"]
