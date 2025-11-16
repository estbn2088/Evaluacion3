from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado = None
        numero1 = int(request.form['numero1'])
        numero2 = int(request.form['numero2'])
        numero3 = int(request.form['numero3'])
        asistencia = int(request.form['asistencia'])
        listanum =[numero1, numero2, numero3]
        promedio = float((numero1 + numero2 + numero3) / 3)
        if (min(listanum) < 10 or max(listanum) > 70) or (asistencia < 0 or asistencia > 100):
            promedio = 0
            resultado = 'Datos Invalidos'
        elif promedio >= 40 and asistencia >= 75:
            resultado = 'APROBADO'
        else:
            resultado = 'REPROBADO'
        return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        resultado = None
        largo = 0
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        if len(nombre1) == len(nombre2):
            resultado = f'{nombre1} y {nombre2}'
            largo = len(nombre1)
        elif len(nombre1)  == len(nombre3):
            resultado = f'{nombre1} y {nombre3}'
            largo = len(nombre1)
        elif len(nombre2) == len(nombre3):
            resultado = f'{nombre2} y {nombre3}'
            largo = len(nombre2)
        elif len(nombre1) > len(nombre2) and len(nombre1) > len(nombre3):
            resultado = nombre1
            largo = len(nombre1)
        elif len(nombre2) > len(nombre1) and len(nombre2) > len(nombre3):
            resultado = nombre2
            largo = len(nombre2)
        else:
            resultado = nombre3
            largo = len(nombre3)
        return render_template('ejercicio2.html', resultado=resultado, largo=largo)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)