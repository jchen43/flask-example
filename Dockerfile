FROM python:3.9.6

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV HOST=0.0.0.0
ENV PORT=80

COPY *.py .

CMD ["python", "app.py"]
