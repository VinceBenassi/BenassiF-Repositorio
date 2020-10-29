# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 4
from PIL import Image as Img, ImageOps as Imo

mar = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/sea.jpg")

def AplicaColor(imagen):
    img = Imo.colorize(mar, black =(93, 138, 168), white="white")
    img.show()

print(AplicaColor(mar))