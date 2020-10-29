# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 1
from PIL import Image,ImageDraw,ImageFilter
from PIL.Image import composite

imagen_1 = Image.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg")
imagen_2 = Image.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_01.jpg")
imagen_3 = Image.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_02.jpg")
imagen_4 = Image.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_03.jpg")
imagen_5 = Image.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_04.jpg")


def img_circulo(img1,img2):
    mascara = Image.new("L",img1.size,0)
    mask_blur = mascara.filter(ImageFilter.GaussianBlur(10))
    draw = ImageDraw.Draw(mask_blur)

    draw.ellipse((160, 60, 350, 250), fill=255)

    img = Image.composite(img1,img2,mask_blur)
    img.show()

print(img_circulo())

def img_rectangulo(img1,img2):
    mascara = Image.new("L",img1.size,0)
    mask_blur = mascara.filter(ImageFilter.GaussianBlur(10))
    draw = ImageDraw.Draw(mask_blur)

    draw.rectangle((130,80,370,230),fill=255)
    img = Image.composite(img1,img2,mask_blur)
    img.show()

print(img_rectangulo(img1,img3))

def img_poligono(img1,img2):
    mascara = Image.new("L",img1.size,0)
    mask_blur = mascara.filter(ImageFilter.GaussianBlur(10))
    draw = ImageDraw.Draw(mask_blur)

    draw.polygon([240,60,140,135,180,255,305,255,345,135,240,60],fill = 255)
    img = Image.composite(img1,img2,mask_blur)
    img.show()

print(img_poligono(img1,img4))

def img_corazon(img1,img2):
    mascara = Image.new("L",img1.size,0)
    mask_blur = mascara.filter(ImageFilter.GaussianBlur(10))
    draw = ImageDraw.Draw(mask_blur)

    draw.pieslice([(245,100),(420,83)],start = 50, end = 250 ,fill = 255)

    img = Image.composite(img1,img2,mask_blur)
    img.show()

print(img_corazon)