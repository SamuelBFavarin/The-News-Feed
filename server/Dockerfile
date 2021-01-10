FROM python:3.8-slim

ENV PROJECT_ENV prod

COPY . ./

RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app