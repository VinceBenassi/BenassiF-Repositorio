# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 6
import numpy as np
from numpy.linalg import linalg
import numpy.polynomial as P
import matplotlib.pyplot as pt

data = np.load("/home/franco-os/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 3/datas/cheby.npy")

x = data[0]
y = data[1]

deg = len(x)-1

A = P.chebyshev.chebvander(x,deg)
c = linalg.solve(A,y)
Resutl = P.Chebyshev(c)
xx = np.linspace(x.min(),x.max(),100)

pt.plot(xx,Resutl(xx),'r',label="Interpolación Chebychev")
pt.scatter(x,y,label="Puntos de datos")
pt.ylabel("F(x)")
pt.xlabel("T(s)")
pt.legend()
pt.show()