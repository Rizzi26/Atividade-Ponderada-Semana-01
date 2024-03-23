from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint

app = Flask(__name__)

router = Blueprint('comandos', __name__)

@app.route('/')
def index():
    print("chamei")
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("toki")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            return redirect(url_for('success'))
        else:
            return render_template('login.html', message='Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@app.route('/success')
def success():
    return '<h1>Login bem-sucedido!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
