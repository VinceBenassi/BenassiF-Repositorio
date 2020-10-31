# Programa que crea un grafo y lo devuelve en formato pdf
# Por Franco Benassi
from graphviz import Graph as gr

grafo = gr('G', filename='euleriano.gv', engine='circo') # engine es el motor gráfico
aristas = int(input("Cantidad de aristas que tiene su grafo: "))

def euler(pdf):
    visitados = [] # Cantidad de nodos visitados
    cola = []
    ciclos = 0
    ContadorNodosAgregados = 0  
    caminos = 0
    acumulador = 0  # Cuenta la cantidad de veces que se ha pasado por un vértice
    nodos_pares = 0

    for nodoinicial in range(aristas):
        nodoinicial = str(input("Ingrese nombre para el nodo inicial: "))
        grafo.attr('node', shape='doublecircle')
        # Función que crea los nodos por separado graficamente
        grafo.node(nodoinicial)

        nodo_llegada = str(input("Nombre un nodo para conectarlo con el anterior: "))
        # Función que conecta los nodos deacuerdo a la decisión del usuario
        grafo.edge(nodoinicial, nodo_llegada)   # edge = arista
        
        #Condición que guarda en nuestro arreglo cola cada nodo ingresado en nuestra variable nodoinicial
        if(aristas >= 1):
            cola.append(nodoinicial)
            ContadorNodosAgregados += 1

    #Doble ciclo for para conseguir los ciclos eulerianos de nuestro grafo
    for indice in range(len(cola)):
        actual = cola[indice]
        for j in range(len(cola)):
            if actual == cola[j]:
                nodos_pares += 1
    if nodos_pares > len(cola):
        ciclos += 1

    #Ciclo for para conseguir los caminos eulerianos de nuestro grafo   
    for elementos in range(len(cola)):
        if(cola[elementos] == nodo_llegada or nodoinicial):
            acumulador += 1
        
    if acumulador >= len(cola):
        caminos += 1

    visitados.append(ContadorNodosAgregados) 
    grafo.attr(label=r'\n\nGrafo Euleriano\n por Franco Benassi', fontsize='12')   
    grafo.view()
    
    print("Los elementos de la cola son los nodos:", cola)
    print("La cantidad de nodos visitados es de:", visitados)
    print("La cantidad de ciclos encontrados es de:", ciclos)
    print("La cantidad de caminos encontrados es de:", caminos)

print(euler(grafo))