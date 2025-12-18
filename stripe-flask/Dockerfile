FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 4003

CMD ["gunicorn", "--bind", "0.0.0.0:4003", "app:app"]