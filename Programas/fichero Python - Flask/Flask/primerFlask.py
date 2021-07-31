from flask import Flask

app = Flask(__name__)

@app.route("/")
def Principal():
    return "<h1> Texto realizado con flask </h1>"

if __name__ == '__main__':
    app.run()

