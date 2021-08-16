FROM python:3.9.6 AS base

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask","run"]
