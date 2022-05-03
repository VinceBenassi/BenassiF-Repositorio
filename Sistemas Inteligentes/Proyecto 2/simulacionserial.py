import serial as sc

leer = sc.Serial('/dev/pts/4',9600)

for e in range(4):
    salir = leer.readline().decode("UTF-8")
    print(salir)