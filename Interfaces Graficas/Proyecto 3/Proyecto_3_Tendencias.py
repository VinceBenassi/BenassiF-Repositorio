# Programa de Franco Benassi
# Proyecto #3 Interfaces Graficas 2020
# Ejercicio 5
import numpy as np
from matplotlib import pyplot as pt
from scipy import signal

tendencia = np.linspace(0,5,100)
x = tendencia + np.random.normal(size=100)
y = signal.detrend(x, type='linear')
pt.figure()
pt.plot(tendencia, x, 'tab:blue',label='Serie sin tendencia')
pt.plot(tendencia,y,'tab:orange',label = 'Serie con tendencia')
pt.legend(prop={'size': 10}, loc='upper left')
pt.show()