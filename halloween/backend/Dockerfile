FROM python:3.9-slim

WORKDIR /app

COPY backend/ /app
COPY frontend/ /frontend

RUN pip install -r /app/requirements.txt

CMD ["python", "app.py"]
