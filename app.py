# app.py
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Configurazione
SUPERSET_LOGIN_URL = "http://localhost:8088/api/v1/security/login"
SUPERSET_GUEST_TOKEN_URL = "http://localhost:8088/api/v1/security/guest_token/"

# Credenziali dell'utente amministratore di Superset
SUP_USER = "admin"
SUP_PASS = "admin"

# Memorizziamo il token JWT qui
cached_jwt = None

def get_superset_jwt():
    global cached_jwt

    # Se già esiste un token, lo riutilizziamo
    if cached_jwt:
        return cached_jwt

    # Altrimenti, effettuiamo il login
    login_data = {
        "username": SUP_USER,
        "password": SUP_PASS,
        "provider": "db"
    }

    response = requests.post(SUPERSET_LOGIN_URL, json=login_data)
    if response.status_code != 200:
        raise Exception("Login fallito su Superset")

    data = response.json()
    cached_jwt = data["access_token"]
    return cached_jwt
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/get_guest_token", methods=["POST"])
def get_guest_token():
    data = request.get_json()
    dashboard_id = data.get("dashboardId")

    if not dashboard_id:
        return jsonify({"error": "Missing dashboard ID"}), 400

    payload = {
        "resources": [
            {"id": dashboard_id, "type": "dashboard"}
        ],
        "rls": [],
        "user": {
            "first_name": "Guest",
            "last_name": "User",
            "username": "guest_user"
        }
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {get_superset_jwt()}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(SUPERSET_GUEST_TOKEN_URL, json=payload, headers=headers)
        response.raise_for_status()
        token_data = response.json()
        return jsonify({"token": token_data["token"]})
    except requests.exceptions.RequestException as e:
        print("Errore nella richiesta:", str(e))
        return jsonify({"error": "Failed to fetch guest token"}), 500
if __name__ == "__main__":
    app.run(debug=True, port=5000)