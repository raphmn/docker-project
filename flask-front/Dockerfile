FROM python:3.11-alpine

WORKDIR /app

# On copie et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# On copie le code
COPY app.py .

EXPOSE 4002
CMD ["gunicorn", "--bind", "0.0.0.0:4002", "app:app"]
