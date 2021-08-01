# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 1
from pylab import e,figure,meshgrid,linspace,nonzero,title,show,sqrt,sin,cos
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as pt
import numpy as np

#1A
x = linspace(-6, 4, 100)
y = linspace(-5, 4, 100)
u, v = meshgrid(x, y)
    
figura = figure()
z = sqrt(4 - (u**2) + (v**2))
z[nonzero(z < 0)] = 0
    
#especificamos que vamos a graficar en 3D
ax = figura.gca(projection='3d')
ax.plot_surface(u, v, z,color='blue')
title('Figura A')
show()


#1B
figura = figure()
ax = Axes3D(figura)
x = linspace(-8, 4, 100)
y = linspace(-8, 4, 100)
x,y = np.meshgrid(x,y)

def efe(x,y):
    return (sin(x)*cos(y))

ax.plot_surface(x,y,efe(x,y),rstride=1,cstride=1,color='orange')
show()


#1C
x = linspace(-4, 4, 100)
y = linspace(-4, 4, 100)
u, v = meshgrid(x, y)

figura = figure()
z = e**(-u**2)*((v**2)+1)
z[nonzero(z < 0)] = 0

ax = figura.gca(projection='3d')
ax.plot_surface(u, v, z,color='darkgreen')
title('Figura c')
show()