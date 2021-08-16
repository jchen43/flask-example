FROM python:3.9.6 AS base

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV SQLALCHEMY_DATABASE_URI=sqlite:////tmp/test.db


### For debugging

FROM base as debugger

RUN pip install debugpy

ENTRYPOINT ["python", "-m", "debugpy", "--listen", "0.0.0.0:2000", "-m", "flask", "run"]

## For regular development

FROM base as primary

CMD ["flask","run"]
