from flask import Flask, render_template as rt, request as rq

app = Flask(__name__)

@app.route("/formulario")
def formulario():
    return rt("formulario.html")

@app.route("/respuesta")
def respuesta():
    valor1 = rq.args.get('nombre')
    minuscula = any(letra.islower() for letra in valor1)
    numero = any(letra.isdigit() for letra in valor1)
    mayuscula = valor1[0].isupper()
    requisitos = minuscula and numero and mayuscula
    return rt("respuesta.html", nombre=valor1, lmin=minuscula, digito=numero, lmay=mayuscula, todo=requisitos)

if __name__ == '__main__':
    app.run(debug=True)