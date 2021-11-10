# Primero en entrar, Primero en salir
# FIFO

colabanco = ["Juan", "Pedro", "Daniela", "Pablo"]

colabanco.append("Jimena")
colabanco.append("Roberto")

print(colabanco)

atencion = colabanco.pop(0)

print("Se está atendiendo a:", atencion)
print(colabanco)