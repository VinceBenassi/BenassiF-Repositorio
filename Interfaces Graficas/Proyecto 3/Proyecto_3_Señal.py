# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 4
from matplotlib.pyplot import axes
import numpy as np
from scipy import signal
import matplotlib.pyplot as pt

señal = np.load("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/datas/signal.npy") 

t = np.linspace(0,len(señal),100)

#Encuentra la media
T_media = signal.medfilt(señal,25)
T_wiener = signal.wiener(señal)

pt.title("Filtro de señales")
pt.plot(t,señal,label="Señal original")
pt.plot(T_media,label="Filtro Media")
pt.plot(t,T_wiener,label="Filtro Wiener")
pt.xlabel("Tiempo(s)")
pt.ylabel("Señal")
pt.legend()
pt.show()