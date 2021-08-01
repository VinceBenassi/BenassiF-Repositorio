# Programa de Franco Benassi
# Proyecto #4 y 5 Sistemas Inteligentes 2020
# Ejercicio 1
from sklearn.cluster import KMeans
import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
 
kmeans_1 = np.load("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 4 y 5/KMeans/A.npy")
kmeans_2 = np.load("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 4 y 5/KMeans/_.npy")

Datos = pd.DataFrame(kmeans_1)

def df(dft):
    Datos.columns = ['x', 'y'] 
    Datos['cluster'] = kmeans_2
    Colores = {0:'red', 1:'green', 2:'blue'}
    Datos['Colores'] = Datos.cluster.map(Colores)

    pt.figure(1)
    pt.title("Figura 1.1") 
    pt.scatter(x='x',y='y',data=Datos)
    pt.ylabel('Feature B')
    pt.xlabel('Feature A')

    pt.figure(2)
    pt.title("Figura 1.2")
    pt.scatter(x='x',y='y',c='Colores',data=Datos)
    pt.ylabel('Feature B')
    pt.xlabel('Feature A')

df(Datos)

pares_ordenados = []
for elementos in range(len(Datos)):
    x = Datos['x'][elementos]
    y = Datos['y'][elementos]
    pares_ordenados.append((x, y))

kmeans = KMeans(n_clusters = 3)
kmeans.fit(pares_ordenados)

print("Los pares ordenados de los centros de cada cluster son los siguientes: \n", kmeans.cluster_centers_)

pt.figure(3)
pt.title("Figura 1.3")
pt.scatter(x='x', y='y', c='Colores', data=Datos)
pt.scatter(x=kmeans.cluster_centers_[:,0], y=kmeans.cluster_centers_[:,1], c="black", marker="*")
pt.ylabel('Feature B')
pt.xlabel('Feature A')

print("\nLas etiquetas son: \n", kmeans.labels_)
print("El número de etiquetas es de:", len(kmeans.labels_))

data_test = [[2,5], [3.2,6.5], [7,2.5], [9,3.2], [9,-6], [11,-8]]
print("La predicción del data_test es de:", kmeans.predict(data_test))

print("\nMuestra de las clases a las que pertenecen los data_test \n")
for i in range(len(data_test)):
    print("Los datos", data_test[i], "pertenecen a la clase", kmeans.predict(data_test)[i])

pt.show()