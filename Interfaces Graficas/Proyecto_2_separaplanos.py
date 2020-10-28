# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 2
from PIL import Image as Img
import math

raiz = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/raiz.jpg")
color = raiz.getdata()
fondo = (0, 0, 0)

def PlanosImagen(imagen):
    rojo = [(red[0], 0, 0) for red in color]
    verde = [(0, green[1], 0) for green in color]
    azul = [(0, 0, blue[2]) for blue in color]
    
    imagen.putdata(rojo)
    imagen.show()
    imagen.save('rojo.png')
    imagen.putdata(verde)
    imagen.show()
    imagen.save('verde.png')
    imagen.putdata(azul)
    imagen.show()
    imagen.save('azul.png')

print(PlanosImagen(raiz))

rosso = Img.open('rojo.png')
verdi = Img.open('verde.png')
azzurro = Img.open('azul.png')

def Area(imagen):
    momen = 0
    for largo in range(imagen.height):
        for ancho in range(imagen.width):
            if (imagen.getpixel((ancho,largo)) != fondo):
                momen += (math.pow(ancho,0)) * (math.pow(largo,0))
    return float(momen)

print("El área de la imagen de plano rojo es:", Area(rosso))
print("El área de la imagen de plano verde es:", Area(verdi))
print("El área de la imagen de plano azul es:", Area(azzurro))