# Programa de Franco Benassi
# Proyecto #4 y 5 Sistemas Inteligentes 2020
# Ejercicio 2
from sklearn.cluster import MeanShift
import matplotlib.pyplot as pt
import numpy as np
import pandas as pd

Meanshift_1 = np.load("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 4 y 5/MeanShift/X.npy")
Meanshift_2 = np.load("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 4 y 5/MeanShift/_ .npy")

Dataframe = pd.DataFrame(Meanshift_1, columns=['x', 'y'])

def df(dtf):
    Dataframe['cluster'] = Meanshift_2
    colores = {0:'red', 1:'green', 2:'blue', 3:'yellow'}
    Dataframe['colores'] = Dataframe.cluster.map(colores)

    pt.figure(1)
    pt.title("Figura 2.1")
    pt.scatter(x='x', y='y', data=Dataframe)
    pt.ylabel('Feature B')
    pt.xlabel('Feature A')

    pt.figure(2)
    pt.title("Figura 2.2")
    pt.scatter(x='x', y='y', c='colores', data=Dataframe)
    pt.ylabel('Feature B')
    pt.xlabel('Feature A')

df(Dataframe)

pares_ordenados = []
for elementos in range(len(Dataframe)):
    x = Dataframe['x'][elementos]
    y = Dataframe['y'][elementos]
    pares_ordenados.append((x, y))

mean = MeanShift(bandwidth=4)
mean.fit(pares_ordenados)
print("Los pares ordenados de los centros de cada cluster son los siguientes: \n", mean.cluster_centers_)

pt.figure(3)
pt.title("Figura 2.3")
pt.scatter(x='x', y='y', c='colores', data=Dataframe)
pt.scatter(x=mean.cluster_centers_[:, 0], y=mean.cluster_centers_[:, 1], c="black", marker="*")
pt.ylabel('Feature B')
pt.xlabel('Feature A')

print("\nLas etiquetas son: \n", mean.labels_)
print("El número de etiquetas es de:", len(mean.labels_))

data_test = [ [-7, -6], [1.5, -6.5], [7.9, 0.5], [5.5, 10] ]
print("La predicción del data_test es de:", mean.predict(data_test))

print("\nMuestra de las clases a las que pertenecen los data_test \n")
for i in range(len(data_test)):
    print("Los datos", data_test[i], "pertenecen a la clase", mean.predict(data_test)[i])

pt.show()