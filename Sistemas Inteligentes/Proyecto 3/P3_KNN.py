# Programa Editado de Franco Benassi
# Proyecto #3 Sistemas Inteligentes 2020
# Ejercicio 1
import math
from math import pi
import pandas as pd

#Ejercicio 1
dTraining = pd.read_csv("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 3/Datas/data_training.txt", sep=",")
DF1 = pd.DataFrame(dTraining)

dTest = pd.read_csv("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 3/Datas/data_test.txt", sep=",")
DF2 = pd.DataFrame(dTest)

dLabel = {0: 'Iris-setosa', 1: 'Iris-versicolor', 2: 'Iris-virginica'}
datos = {0:[],1:[],2:[]}

def KNN(DatosArreglos, prueba, contador):
    arreglo = []
    for e in DatosArreglos:
        for i in DatosArreglos[e]:
            dE = math.sqrt( (i[0] - prueba[0])**2 + (i[1] - prueba[1])**2)
            arreglo.append((dE, e))
        arreglo = sorted(arreglo)[:contador]
        v1 = v2 = v3 = 0

    for d in arreglo:
        if d[1] == 0:
            v1 += 1
        elif d[1] == 1:
            v2 += 1
        else:
            v3 += 0
            
    if (v1 > v2) and (v1 > v3):
        return dLabel[0]
    elif (v2 > v1) and (v2 > v1): 
        return dLabel[1]
    elif (v3 > v1) and (v3 > v2):
        return dLabel[2]



def datatext(label):
    Test = []
    for elementos in range(len(DF2)):
        x1 = DF2["x1"].values[elementos]
        x2 = DF2["x2"].values[elementos]
        x3 = DF2["x3"].values[elementos]
        x4 = DF2["x4"].values[elementos]
        Test.append([x1,x2,x3,x4])

    for elementos in DF1.index:
        x1 = DF1["x1"].values[elementos]
        x2 = DF1["x2"].values[elementos]
        x3 = DF1["x3"].values[elementos]
        x4 = DF1["x4"].values[elementos]

        if(DF1["Clase"].values[elementos] == 0):
            datos[0].append((x1,x2,x3,x4))

        elif(DF1["Clase"].values[elementos] == 1):
            datos[1].append((x1,x2,x3,x4))

        elif(DF1["Clase"].values[elementos] == 2):
            datos[2].append((x1,x2,x3,x4))

    for aTest in Test:
        print(KNN(datos, aTest, 3))

print(datatext(dLabel))
#Fin ejercicio 1