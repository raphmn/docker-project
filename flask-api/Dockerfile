# 1. Utilisation d'une image de base stable
FROM python:3.11-alpine

# 2. Définition du dossier de travail (crée le dossier s'il n'existe pas)
WORKDIR /app

# 3. Copie du fichier requirements.txt depuis la machine hôte vers /app/
COPY requirements.txt .

# 4. Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie de tout le code source dans le dossier /app
COPY . .

# 6. Commande de lancement (adapter selon le nom de ton fichier python)
EXPOSE 4001
CMD ["gunicorn", "--bind", "0.0.0.0:4001", "app:app"]
