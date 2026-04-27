FROM python:3.11-slim

WORKDIR /app
COPY app/ .

RUN pip install flask gunicorn

CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
