# main.py
from flask import Flask
from tinydb import TinyDB
from routers import comandos, logs

app = Flask(__name__)

db = TinyDB('comandos.json')

app.register_blueprint(comandos.router)
app.register_blueprint(logs.router)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=False)
