FROM python:3.9

RUN mkdir /search_app/
WORKDIR /search_app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY data data
COPY src src

CMD ["python", "src/search/main.py"]