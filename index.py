from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def res():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/reser')
def reser():
    return render_template('reserva.html')

@app.route('/solucion', methods=['GET', 'POST'])
def solucion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        
        return render_template('mensaje.html')


if __name__ == '__main__':
    app.run(port=5030)