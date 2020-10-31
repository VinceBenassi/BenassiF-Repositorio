# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 1
from PIL import Image as Img, ImageDraw as ID, ImageFilter as IF
from PIL.Image import composite

imagen_1 = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg")
imagen_2 = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_01.jpg")
imagen_3 = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_02.jpg")
imagen_4 = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_03.jpg")
imagen_5 = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_04.jpg")


def EfectoCirculo(imagen,imagen2):
    mascara = Img.new("L",imagen.size,0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.ellipse((160, 60, 350, 250), fill=255)

    img = Img.composite(imagen,imagen2,desenfoque)
    img.show()

print(EfectoCirculo(imagen_1, imagen_2))


def EfectoRectángulo(imagen,imagen2):
    mascara = Img.new("L",imagen.size,0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.rectangle((130,80,370,230),fill=255)
    img = Img.composite(imagen,imagen2,desenfoque)
    img.show()

print(EfectoRectángulo(imagen_1,imagen_3))


def EfectoPentágono(imagen,imagen2):
    mascara = Img.new("L",imagen.size,0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.polygon([240,60,140,135,180,255,305,255,345,135,240,60],fill = 255)
    img = Img.composite(imagen,imagen2,desenfoque)
    img.show()

print(EfectoPentágono(imagen_1,imagen_4))


def EfectoCorazón(imagen,imagen2):
    mascara = Img.new("L",imagen.size,0)
    desenfoque = mascara.filter(IF.GaussianBlur(10))
    dibuja = ID.Draw(desenfoque)

    dibuja.pieslice([(245,100),(420,83)],start = 50, end = 250 ,fill = 255)

    img = Img.composite(imagen,imagen2,desenfoque)
    img.show()

print(EfectoCorazón(imagen_1, imagen_5))