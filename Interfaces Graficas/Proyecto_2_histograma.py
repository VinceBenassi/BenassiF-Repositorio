# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 3
from matplotlib import pyplot as pt
from PIL import Image as Img

chica = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg")
foto = Img.open('/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg').convert('L')

def histograma(foto):
    r,g,b = foto.split()
    foto.show()  
    pt.plot(r.histogram(),color='r')  
    pt.plot(g.histogram(),color='g')   
    pt.plot(b.histogram(),color='b')
    pt.xlabel("Intensidad del color")
    pt.ylabel("Cantidad de pixeles")
    pt.show()

def mostrar_histograma(foto):
    histograma = foto.histogram()
    x = range(len(histograma))
    pt.title("Grafica de histograma escala a grises")
    pt.ylabel("Numero de pixeles")
    pt.xlabel("Valores de intencidad")
    pt.scatter(x,histograma)
    pt.bar(x,histograma,align='center')
    pt.show()