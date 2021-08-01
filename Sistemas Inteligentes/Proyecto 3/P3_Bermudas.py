# Programa de Franco Benassi
# Proyecto #3 Sistemas Inteligentes 2020
# Ejercicio 3
import matplotlib.pyplot as pt
from matplotlib.pyplot import xcorr
from sklearn.cluster import KMeans
import pandas as pd

data = pd.read_csv("/home/franco-os/Documentos/Informática/Sistemas Inteligentes/Proyecto 3/Datas/body.csv", sep=",")
DataFrame = pd.DataFrame(data)
DataFrame = DataFrame.drop(columns=['id', 'seqn', 'bmdstats','bmxwt','bmiwt','bmxrecum','bmirecum','bmxhead','bmihead','bmxht','bmiht','bmxbmi','bmdbmic','bmileg','bmxarml','bmiarml','bmxarmc','bmiarmc','bmiwaist','bmxsad1','bmxsad2','bmxsad3','bmxsad4','bmdavsad','bmdsadcm'])

for nulos in DataFrame.index:
    if(((pd.isnull(DataFrame["bmxwaist"][nulos])==True) or pd.isnull(DataFrame["bmxleg"][nulos])==True)):
        DataFrame = DataFrame.drop([nulos],axis=0)

pt.figure(1)
pt.title("Conjunto Original")
pt.scatter(DataFrame["bmxleg"],DataFrame["bmxwaist"],c=['r'])
pt.xlabel("Longitud de Piernas(cm)")
pt.ylabel("Circunferecia de Cintura(cm)")

arreglo = [] 
for elementos in range(len(DataFrame)):
    ejeX = DataFrame["bmxleg"].values[elementos]
    ejeY= DataFrame["bmxwaist"].values[elementos]
    arreglo.append([ejeX, ejeY])


#Diseño de 2 bermudas
media_k2 = KMeans(n_clusters=2)
media_k2.fit(arreglo)
print("Dimensiones para los diseños de 2 bermudas: ")
print(media_k2.cluster_centers_)

pt.figure(2)
pt.scatter(DataFrame["bmxleg"],DataFrame["bmxwaist"],c=media_k2.labels_,cmap='Dark2',s=1)
pt.scatter(media_k2.cluster_centers_[:,0],media_k2.cluster_centers_[:,1],color="black")
pt.xlabel("Longitud de Piernas(cm)")
pt.ylabel("Circunferencia de Cintura(cm)")
pt.title("Diseño para 2 bermudas")


#Diseño de 4 bermudas
media_k4 = KMeans(n_clusters=4)
media_k4.fit(arreglo)
print("Dimensiones para los diseños de 4 bermudas")
print(media_k4.cluster_centers_)

pt.figure(3)
pt.scatter(DataFrame["bmxleg"],DataFrame["bmxwaist"],c=media_k4.labels_,cmap='winter',s=1)
pt.scatter(media_k4.cluster_centers_[:,0],media_k4.cluster_centers_[:,1],color="black")
pt.xlabel("Longitud de Piernas(cm)")
pt.ylabel("Circunferencia de Cintura(cm)")
pt.title("Diseño para 4 bermudas")
pt.show()