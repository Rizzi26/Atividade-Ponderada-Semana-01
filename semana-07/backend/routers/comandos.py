from flask import Blueprint, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
from classes.robot import RobotClass
from datetime import datetime

router = Blueprint('comandos', __name__)

db = TinyDB("db/logs.json")

comandos_table = db.table("logs")

# robo = RobotClass()

@router.route('/')
def index():
    return render_template("index.html")

@router.route('/movimentar', methods=['POST'])
def movimentar():
    dados = request.json

    x = dados.get('x')
    y = dados.get('y')
    z = dados.get('z')

    if x == None or y == None or z == None:
        registrar_comando("não foi possível movimentar o robô para a posição desejada", x=x, y=y, z=z)
        return redirect(url_for('index.html'))
    else:
        x = float(x)
        y = float(y)
        z = float(z)
        registrar_comando("movimentar", x=x, y=y, z=z)
        #robo.move_to(x, y, z, 0)

    
    print(f'Valor de x: {x}, Valor de y: {y}, Valor de z: {z}')

    return render_template('index.html')

@router.route('/ligar-ferramenta', methods=['POST'])
def ligar_ferramenta():
    dados = request.json

    ligar = dados.get('ligar')

    if ligar == True:
        registrar_comando("ligando ferramenta", ligar=ligar)
        #robo.ligar_ferramenta()
        print(f'Ferramenta ligada!')
    else:
        registrar_comando("não foi possível ligar a ferramenta", ligar=ligar)
        print(f'Não foi possível ligar a ferramenta!')

    return render_template('index.html')

@router.route('/desligar-ferramenta', methods=['POST'])
def desligar_ferramenta():
    dados = request.json

    desligar = dados.get('desligar')

    if desligar == True:
        registrar_comando("desligando ferramenta", desligar=desligar)
        #robo.desligar_ferramenta()
        print(f'Ferramenta desligada!')
    else:
        registrar_comando("não foi possível desligar a ferramenta", desligar=desligar)
        print(f'Não foi possível desligar a ferramenta!')

    return render_template('index.html')

@router.route('/home', methods=['POST'])
def home():
    dados = request.json

    voltar = dados.get('voltar')

    if voltar == True:
        #robo.move_to(243.84, 5.12, 157.94, 0)
        registrar_comando("voltando para a home", voltar=voltar, x=243.84, y=5.12, z=157.94)
        print(f'Voltando para a posição inicial!')
    else:
        registrar_comando("não foi possível voltar para home", voltar=voltar)
        print(f'Não foi possível voltar para a posição inicial!')

    return render_template('index.html')

def registrar_comando(comando, **kwargs):
    now = datetime.now()
    data_hora = now.strftime("%d/%m/%Y %H:%M:%S")
    registro = {"comando": comando, "data_hora": data_hora}
    registro.update(kwargs)
    db.insert(registro)