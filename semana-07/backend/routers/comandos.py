from flask import Blueprint, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
from classes.robot import RobotClass

router = Blueprint('comandos', __name__)

db = TinyDB("db/comandos.json")

comandos_table = db.table("comandos")

@router.route('/')
def index():
    return render_template("login.html")

@router.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        User = Query()

        user = comandos_table.search((User.username == username))

        if user:
            return '<h1>Usuário já cadastrado!</h1>'
        else:
            comandos_table.insert({'username': username, 'password': password})
            return redirect(url_for('comandos.success'))

    return render_template('login.html')

@router.route('/delete-login', methods=['POST'])
def delete_login():
    if request.method == 'POST':
        username = request.form['username']

        User = Query()

        user = comandos_table.search((User.username == username))

        if user:
            comandos_table.remove((User.username == username))
            return '<h1>Usuário deletado!</h1>'
        else:
            return '<h1>Usuário não encontrado!</h1>'

@router.route('/success')
def success():
    return '<h1>Cadastro bem-sucedido!</h1>'
