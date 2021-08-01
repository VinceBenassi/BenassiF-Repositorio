from flask import Flask

app = Flask(__name__)

@app.route("/")
def Principal():
    return "<h1> Texto realizado con flask </h1>"

@app.route("/adios")
def despedirse():
    return "<h3>Hasta Luego, nos vemos</h3>"

# Ruta Dinámica
@app.route("/saludar/<nombre>")
def saludar(nombre):
    return "<h1>Hola</h1>"+ nombre + "<h1>Buenas Tardes!!</h1>"

if __name__ == '__main__':
    app.run()

