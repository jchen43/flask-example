FROM python:3.9.6 AS base

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV HOST=0.0.0.0
ENV PORT=80

COPY *.py .

### For debugging

FROM base as debugger

RUN pip install debugpy

ENTRYPOINT ["python", "-m", "debugpy", "--listen", "0.0.0.0:2000", "app.py"]

## For regular development

FROM base as primary

CMD ["python", "app.py"]
