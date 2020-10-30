# Programa que crea un grafo y lo devuelve en formato pdf
# Por Franco Benassi
from graphviz import Graph as gr

grafo = gr('G', filename='euleriano.gv', engine='circo') # engine es el motor gráfico
aristas = int(input("Cantidad de aristas que tiene su grafo: "))

def euler(pdf):
    visitados = []
    cola = []
    ciclos = 0
    cont = 0  # Cantidad de nodos visitados
    caminos = 0

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
            cont += 1

        if(cola[0] == nodo_siguiente):
            ciclos = caminos / aristas
            
        for elementos in range(len(cola)):
            if(cola[elementos] == nodo_siguiente or nodoinicial):
                caminos += 1

    visitados.append(cont) 
    grafo.attr(label=r'\n\nGrafo Euleriano\n por Franco Benassi', fontsize='12')   
    grafo.view()
    
    print("Los elementos de la cola son los nodos:", cola)
    print("La cantidad de nodos visitados es de:", visitados)
    print("La cantidad de ciclos encontrados es de:", ciclos)
    print("La cantidad de caminos encontrados es de:", caminos)

print(euler(grafo))