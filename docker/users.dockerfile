# syntax=docker/dockerfile:1

FROM python:latest

ARG USERS_DATA_PATH

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY search /app/search
COPY data /app/data

EXPOSE 7999

ENV USERS_DATA_PATH=$USERS_DATA_PATH

CMD ["uvicorn", "search.services.users.main:app", "--host", "0.0.0.0", "--port", "7999"]
