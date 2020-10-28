# Programa que crea un grafo y lo devuelve en formato pdf
# Por Franco Benassi
from graphviz import Graph as gr

grafo = gr('G', filename='euleriano.gv', engine='sfdp')
aristas = int(input("Cantidad de aristas que tiene su grafo: "))

def euler(pdf):
    for creaGrafo in range(aristas):
        creaGrafo = str(input("Ingrese nombre para un nodo: "))
        grafo.attr('node', shape='doublecircle')
        # Función que crea los nodos por separado graficamente
        grafo.node(creaGrafo)
        nodo = str(input("Nombre un nodo para conectarlo con el anterior: "))
        # Función que conecta los nodos deacuerdo a la decisión del usuario
        grafo.edge(creaGrafo, nodo)     
    grafo.view()
    
print(euler(grafo))

