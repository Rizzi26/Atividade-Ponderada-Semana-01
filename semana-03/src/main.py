import inquirer
import typer
import sys
from pydobot import Dobot
from serial.tools import list_ports
from yaspin import yaspin

# iniciando o spinner para mostrar que o programa está processando
spinner = yaspin(text="Processando...", color="red")
app = typer.Typer()


class RobotClass:
    # Inicializando o robô
    def __init__(self):
        self.port = self.scan_ports()
        self.robo = Dobot(port=self.port)
        self.robo.speed(100, 100)
        posicao_atual = self.robo.pose()    
        print(f"Posição inicial {posicao_atual}")

    # Função para pegar a posição atual do robô
    def posição_atual(self):
        return self.robo.pose()

    # Função para mover o robô para uma posição específica
    def move_to(self, x, y, z, r, wait=True):
        self.robo.move_to(x, y, z, r)

    # Função para ligar a ferramenta
    def ligar_ferramenta(self):
        self.robo.suck(True)
    
    # Função para desligar a ferramenta 
    def desligar_ferramenta(self):
        self.robo.suck(False)

    # Função para escanear as portas e encontrar o robô
    def scan_ports(self):
        ports = list_ports.comports()
        for port in ports:
            print(f"Trying port {port.device}")
            try:
                robot = Dobot(port=port.device)
                robot.close()
                print(f"Found robot at {port.device}")
                return port.device
            except:
                print(f"No robot found at {port.device}")
        raise Exception("No robot found")

# Função para iniciar a interface do robô
@app.command(name="interface")
def interface():
    robo = RobotClass()
    posicao_inicial = robo.posição_atual()
    choices = ["Ligar ferramenta", "Movimentar", "Posição atual", "Sair"]

    while True:
        perguntas = [
            inquirer.List("interface", message="Qual comando você quer executar ?", choices=choices),
        ]

        respostas = inquirer.prompt(perguntas)
        choices = processar(respostas, robo, posicao_inicial, choices)

# Função para processar os comandos
def processar(dados, robo, posicao_inicial, choices):
    comando = dados["interface"]

    if comando == "Sair": 
        sys.exit()

    if comando == "Voltar para posição inicial":
        spinner.start()
        robo.move_to(243.84, 5.12, 157.94, 0)
        spinner.stop()

        if "Voltar para posição inicial" in choices:
            choices.remove("Voltar para posição inicial")

    elif comando == "Ligar ferramenta":
        spinner.start()
        robo.ligar_ferramenta()
        spinner.stop()

        if "Ligar ferramenta" in choices:
            choices.remove("Ligar ferramenta")
            choices.insert(0, "Desligar ferramenta")

    elif comando == "Desligar ferramenta":
        spinner.start()
        robo.desligar_ferramenta()
        spinner.stop()

        if "Desligar ferramenta" in choices:
            choices.remove("Desligar ferramenta")
            choices.insert(0, "Ligar ferramenta")
    
    elif comando == "Movimentar":
            distancia_x = float(typer.prompt("Digite a distância a ser movida no eixo X:"))
            distancia_y = float(typer.prompt("Digite a distância a ser movida no eixo Y:"))
            distancia_z = float(typer.prompt("Digite a distância a ser movida no eixo Z:"))
            distancia_r = float(typer.prompt("Digite a distância a ser movida na rotação:"))
            nova_posicao_x = posicao_inicial[0] + distancia_x
            nova_posicao_y = posicao_inicial[1] + distancia_y
            nova_posicao_z = posicao_inicial[2] + distancia_z
            nova_posicao_r = posicao_inicial[3] + distancia_r
            spinner.start()
            robo.move_to(nova_posicao_x, nova_posicao_y, nova_posicao_z, nova_posicao_r, wait=True)

            if "Voltar para posição inicial" not in choices:
                choices.insert(3, "Voltar para posição inicial")

            spinner.stop()
            print(f"Movendo: X={nova_posicao_x}, Y={nova_posicao_y}, Z={nova_posicao_z}, R={nova_posicao_r} unidades")

    elif comando == "Posição atual":
        spinner.start()	
        posicao_atual = robo.posição_atual()
        spinner.stop()
        print(f"Posição atual {posicao_atual}")

    return choices

if __name__ == "__main__":
    app()