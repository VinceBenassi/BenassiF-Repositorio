# Programa que crea un grafo y lo devuelve en formato pdf
# Por Franco Benassi
from graphviz import Graph as gr

grafo = gr('G', filename='euleriano.gv', engine='circo') # engine es el motor gráfico
aristas = int(input("Cantidad de aristas que tiene su grafo: "))

def euler(pdf):
    visitados = []
    cola = []
    for nodoinicial in range(aristas):
        nodoinicial = str(input("Ingrese nombre para el nodo inicial: "))
        grafo.attr('node', shape='doublecircle')
        # Función que crea los nodos por separado graficamente
        grafo.node(nodoinicial)
        nodo_siguiente = str(input("Nombre un nodo para conectarlo con el anterior: "))
        # Función que conecta los nodos deacuerdo a la decisión del usuario
        grafo.edge(nodoinicial, nodo_siguiente)   # edge = arista
        
        if(aristas >= 1):
            cola.append(nodoinicial)
            visitados.append(cont = 0)

        grafo.attr(label=r'\n\nGrafo Euleriano\n por Franco Benassi', fontsize='12')
    grafo.view()
    print(cola)
    
print(euler(grafo))




#try:
    #aristas = 0
    #print("No se puede realizar un recorrido")
#except:
    #aristas >= 1

