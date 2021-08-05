from flask import Flask, render_template as rt

app = Flask(__name__)

@app.route("/")
def comienzo():
    valorNombre = "Franco"
    valorEdad = "21"
    diccionario = {'nombre':'Franco', 'edad':'21'}
    return rt("main.html", datos=diccionario)

@app.route("/sumando/<valor1>/<valor2>")
def portada(valor1, valor2):
    suma = int(valor1) + int(valor2)
    return rt("portada.html", resultado=str(suma))

if __name__ == '__main__':
    app.run(debug=True)