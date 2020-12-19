# Programa de Franco Benassi
# Proyecto #4 y 5 Sistemas Inteligentes 2020
# Ejercicio 3
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

Peso = [[60.0, 65.0, 72.3, 75.0, 80.0]]
Altura = [[1.60, 1.65, 1.70, 1.73, 1.80]]
test_altura = [[1.58, 1.62, 1.69, 1.76, 1.82 ]]

regresion = LinearRegression()
regresion.fit(Altura, Peso)

print(regresion.predict(test_altura))

RSS = ((regresion.predict(test_altura) - test_altura)**2).sum()
print("El valor del RSS predictor es de:", RSS)