# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 2
from matplotlib import pyplot as pt
import numpy
import cv2 as cv

raiz = cv.imread("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/raiz.jpg")

#Separando por canales de colores la imagen
def CanalRojo(imagen):
    pt.imshow(imagen[:, :, 0])
    pt.title("Escala Roja de la imagen")
    pt.figure()

print(CanalRojo(raiz))

def CanalVerde(imagen):
    separacolor = cv.cvtColor(imagen, cv.COLOR_BGR2HSV)
    cv.imshow("Escala Verde de la imagen", separacolor)

print(CanalVerde(raiz))

def CanalAzul(imagen):
    pt.imshow(imagen[:, :, 2])
    pt.title("Escala Azul de la imagen")

print(CanalAzul(raiz))

pt.show()
cv.waitKey(0)