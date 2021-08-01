# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 1
from PIL import Image as Img, ImageDraw as ID, ImageFilter as IF
from PIL.Image import composite

imagen_1 = Img.open("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg")
imagen_2 = Img.open("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_01.jpg")
imagen_3 = Img.open("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_02.jpg")
imagen_4 = Img.open("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_03.jpg")
imagen_5 = Img.open("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_04.jpg")


def EfectoCirculo(imagen, imagen2):
    mascara = Img.new("L", imagen.size, 0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.ellipse((160, 60, 350, 250), fill = 255)

    img = Img.composite(imagen, imagen2, desenfoque)
    img.show()

print(EfectoCirculo(imagen_1, imagen_2))


def EfectoRectángulo(imagen, imagen2):
    mascara = Img.new("L", imagen.size, 0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.rectangle((130,80,370,230),fill = 255)
    img = Img.composite(imagen, imagen2, desenfoque)
    img.show()

print(EfectoRectángulo(imagen_1, imagen_3))


def EfectoPentágono(imagen, imagen2):
    mascara = Img.new("L", imagen.size, 0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.polygon([240,60,140,135,180,255,305,255,345,135,240,60],fill = 255)
    img = Img.composite(imagen, imagen2, desenfoque)
    img.show()

print(EfectoPentágono(imagen_1, imagen_4))


def EfectoCorazón(imagen, imagen2):
    mascara = Img.new("L", imagen.size, 0)
    dibuja = ID.Draw(mascara)
    ancho = 500 
    largo = 250

    polígono = [
        (ancho / 100, largo / 3),
        (ancho / 10, 81 * largo / 120),
        (ancho / 2, largo),
        (ancho - ancho / 10, 81 * largo / 120),
        (ancho - ancho / 10, largo / 3),
    ]
    dibuja.polygon(polígono, fill = 255)

    dibuja.ellipse((0, 0,  ancho / 2, 3 * largo / 4), fill = 255)
    dibuja.ellipse((ancho / 2, 0,  ancho, 3 * largo / 4), fill = 255)

    img = Img.composite(imagen, imagen2, mascara)
    img.show()

print(EfectoCorazón(imagen_1, imagen_5))