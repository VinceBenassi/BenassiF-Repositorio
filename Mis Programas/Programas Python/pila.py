# Ultimo en entrar, Primero en salir
# LIFO

pila = [1, 2, 3, 4]

pila.append(5)
pila.append(6)

print(pila)

print("Atendiendo al ultimo elemento de la pila")
pila.pop()

print(pila)