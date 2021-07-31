# Funciones Decoradoras

def asteriscos(funcion):
    def colocarAsteriscos():
        print("*****************")
        funcion()
        print("*****************")
    return colocarAsteriscos

@asteriscos
def imprimir():
    print("hola, que tal?")

imprimir()