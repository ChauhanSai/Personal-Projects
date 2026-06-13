from dotenv import load_dotenv
import requests
import webbrowser
import urllib.parse
import uuid
import os
import base64

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

from flask import Flask, jsonify, request

app = Flask(__name__)

from flask_cors import CORS

CORS(app)

@app.route('/authorize', methods=['GET'])
def authorize():
    state = str(uuid.uuid4())
    env = open("auth.env", "w")
    env.write(f"STATE={state}\n")

    params = {
        "client_id": client_id,
        "redirect_uri": "http://127.0.0.1:8080/api/auth",
        "response_type": "code",
        "state": state,
        "scope": "playlist-read-private playlist-modify-public playlist-modify-private"
    }

    base_url = "https://accounts.spotify.com/authorize"
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(url)

    webbrowser.open(url)

    env.close()

    return {"status": 200, "state": state}

@app.route('/api/auth', methods=['GET'])
def auth():
    try:
        code = request.args.get('code')
        state = request.args.get('state')
    except:
        code = None
        state = None

    if code is None:
        return {"status": 401, "error": "Missing 'code' parameter"}
    else:
        env = open("auth.env", "r")
        this_state = env.readline().strip().split("=")[1]
        env.close()
        if state != this_state:
            return {"status": 401, "error": "Invalid 'state' parameter"}

    print(code)

    auth_header = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    exchange = requests.post("https://accounts.spotify.com/api/token", data={
        "code": code,
        "redirect_uri": "http://127.0.0.1:8080/api/auth",
        "grant_type": "authorization_code"
    }, headers={
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    })

    print(exchange.json())

    if exchange.status_code != 200:
        return {"status": 401, "error": "Authorization failed", "code": code}

    access_token = exchange.json()["access_token"]
    refresh_token = exchange.json()["refresh_token"]

    env = open("auth.env", "w")
    env.write(f"ACCESS_TOKEN={access_token}\n")
    env.write(f"REFRESH_TOKEN={refresh_token}\n")
    env.close()

    return {"status": 200, "access_token": access_token, "refresh_token": refresh_token}

@app.route('/token', methods=['GET'])
def token():

    return {"status": 200}

if __name__ == '__main__':
    app.run(debug=True, port=8080)

    # DEBUG