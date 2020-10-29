# Programa de Franco Benassi
# Proyecto #2 Interfaces Graficas 2020
# Ejercicio 3
from PIL import Image as Img
from matplotlib import pyplot as pt

chica = Img.open("/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg")
coversion = Img.open('/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 2/fig_00.jpg').convert('L')

def Graficar_Histograma(imagen):
    r,g,b = imagen.split()
    imagen.show()
    pt.plot(r.histogram(),color='r')
    pt.plot(g.histogram(),color='g')
    pt.plot(b.histogram(),color='b')
    pt.xlabel("Intensidad Colores")
    pt.ylabel("Cantidad de Pixeles")
    pt.show()

print(Graficar_Histograma(chica))

def HistogramaEscalaGrises(imagen):
    Histograma = imagen.histogram()
    longitudHist = range(len(Histograma))
    pt.title("Histograma en Escala de Grises")
    pt.ylabel("Cantidad de Pixeles")
    pt.xlabel("Intensidad de Tonalidades")
    pt.scatter(longitudHist,Histograma)
    pt.bar(longitudHist,Histograma,align='center')
    pt.show()

print(HistogramaEscalaGrises(coversion))