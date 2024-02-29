# ola-flask-api.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ping")
def ping():
    return "pong"

@app.route('/echo', methods=['POST'])
def echo():
    return jsonify(request.json)

@app.route("/soma")
def soma():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"resultado": a + b})

@app.route("/subtracao")
def subtracao():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"resultado": a - b})

@app.route("/multiplicacao")
def multiplicacao():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"resultado": a * b})

@app.route("/divisao", methods=["POST"])
def divisao():
    dados = request.json
    a = int(dados.get("a"))
    b = int(dados.get("b"))
    return jsonify({"resultado": a / b})
