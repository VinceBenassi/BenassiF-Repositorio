# Programa que crea un grafo y lo devuelve en formato pdf
# Por Franco Benassi
from graphviz import Graph as gr

euler = gr('G', filename='euleriano.gv', engine='sfdp')
nodos = int(input("Cantidad de nodos que tiene el grafo: "))

def grafo(pdf):
    for creaGrafo in range(nodos):
        creaGrafo = str(input("Ingrese un nodo: "))
        euler.node(creaGrafo)
        final = str(input("Con cual nodo quieres conectar el inicio: "))
        euler.edge(creaGrafo, final)       
    euler.view()

print(grafo(euler))

