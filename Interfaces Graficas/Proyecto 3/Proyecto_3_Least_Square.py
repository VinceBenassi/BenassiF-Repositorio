# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 3
from matplotlib.pyplot import figure
import numpy as np
from numpy.lib.polynomial import polyval
from pylab import *

recorrido = np.load("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/datas/f1.npy")
recorrido2 = np.load("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/datas/f2.npy")
x = np.arange(start=1,stop=50,step=1)
z = np.polyfit(x,recorrido,1)
z_2 = np.polyfit(x,recorrido2,2)

figure()
plot(x,recorrido,'o')
plot(x,recorrido2,'o')
plot(x,polyval(z,x),'-')
plot(x,polyval(z_2,x),'-')
show()