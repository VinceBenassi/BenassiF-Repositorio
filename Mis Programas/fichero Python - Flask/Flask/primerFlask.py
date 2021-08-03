from flask import Flask

app = Flask(__name__)

@app.route("/")
def Principal():
    return "<h1> Texto realizado con flask </h1>"

@app.route("/adios")
def despedirse():
    return "<h3>Hasta Luego, nos vemos</h3>"

# Rutas Dinámicas
@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "<h1>Hola</h1>"+ nombre[3] + "<h1>Buenas Tardes!!</h1>"

@app.route("/longitud/<nombre>")
def verLongitud(nombre):
    return "<h3>La longitud de este nombre es de</h3>" + str(len(nombre))+ "<h3>letras</h3>"

@app.route("/edad/<nombre>/<edad>")
def verEdad(nombre, edad):
    return nombre + "<h3>tiene</h3>" + str(edad) + "<h3>años</h3>"

@app.route("/suma/<numeroP>/<numeroS>")
def sumar(numeroP, numeroS):
    suma = int(numeroP) + int(numeroS)
    return "<h3>La suma de</h3>" + str(numeroP) + "<h3>y</h3>" + str(numeroS) + "<h3>es</h3>" + str(suma)

if __name__ == '__main__':
    app.run()

