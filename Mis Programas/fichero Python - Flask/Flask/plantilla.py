from flask import Flask, render_template as rt, request as rq

app = Flask(__name__)

# Uso de diccionario
@app.route("/")
def comienzo():
    valorNombre = "Franco"
    valorEdad = "21"
    diccionario = {'nombre':'Franco', 'edad':'21'}
    return rt("main.html", datos=diccionario)

# Suma de valores usando rt
@app.route("/sumando/<valor1>/<valor2>")
def portada(valor1, valor2):
    suma = int(valor1) + int(valor2)
    return rt("portada.html", resultado=str(suma))

# Uso de bucle FOR
@app.route("/colores")
def colores():
    listaColores = ["verde", "rojo", "amarillo", "azul"]
    return rt("colores.html", colores=listaColores)

# Condicionales
@app.route("/frase/<texto>")
def frase(texto):
    return rt("frase.html", tipo=texto)

# Herencia
@app.route('/herencia')
def herencia():
    return rt('herencia.html')

@app.route('/herencia2')
def herencia2():
    return rt('herencia2.html')

# Formularios
@app.route("/formulario")
def formulario():
    return rt("formulario.html")

@app.route("/agradecimiento")
def agradecimiento():
    valor1 = rq.args.get('nombre')
    valor2 = rq.args.get('apellidos')
    return rt("gracias.html", nombre=valor1, apellidos=valor2)

# Tratamiento de Errores, error 404
@app.errorhandler(404)
def paginaNoEncontrada(error):
    return rt('pagina404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)