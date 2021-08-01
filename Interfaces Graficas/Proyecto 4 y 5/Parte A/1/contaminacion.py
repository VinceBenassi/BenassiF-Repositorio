# Programa de Franco Benassi
# Proyecto #4 y 5 Interfaces Graficas 2020
# Ejercicio 1
import requests as req
import time as ti 
import random as ra

URL = 'http://127.0.0.1:5000/datillos'

def Generate():                         #Datos Ambientales
    datos = {'01': [ra.randint(+5, +20) for aleatorios in range(20)], # MP 1.0 ug/m3
             '25': [ra.randint(+5, +20) for aleatorios in range(20)], # MP 2.5 ug/m3
             '10': [ra.randint(+5, +20) for aleatorios in range(20)], # MP 10 ug/m3
             'te': [ra.randint(-10, +10) for aleatorios in range(20)] # Temperatura
            }
    return datos 

while 1:
    datos = Generate()
    conexion = req.post(URL, json=datos)
    ti.sleep(5)
conexion.close()