# Variables Locales y Globales

# Variables Globales
numero = 45
texto = "hola, que tal?"

 # Variables Locales - Ejemplo, variables de una función
def funcion1():
    numero2 = 24
    saludo = "buenas tardes"
    print(numero2)
    print(saludo)
    print(locals())

funcion1()
print(globals())