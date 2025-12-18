from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def api():
    return jsonify(message="Je suis l’api")

@app.route('/')
def home():
    return "Vous etes sur l'accueil de l'api. Pour acceder y acceder ajoutez /api dans l'url."
