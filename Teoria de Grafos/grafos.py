import math 
from collections import deque


class Graph:
    def _init_(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range (0)]

    def pintar_matriz (self,m,texto):
        cadena = ""

        for c in range(len(m)):
            cadena += "\t" + str(self.vertices[c])

        cadena += "\n " 

        for f in range(len(m)):
            cadena += "\n" + str(self.vertices[f]) + " |"
            for c in range(len(m)):
                if texto:
                    cadena += "\t" + str(m[f][c])
                else:
                    if f == c and (m[f][c] is None or m[f][c] == 0):
                        cadena += "\t" + "\\"
                    else:
                        if m[f][c] is None or math.isinf(m[f][c]):
                            cadena += "\t" + "X"
                        else:
                            cadena += "\t" + str(m[f][c])

        cadena += "\n"
        print(cadena)
    
    def esta_en_vertices(self,v):
        if self.vertices.count(v) == 0:
            return False
        return True

    def agregar_vertices(self,v):
        if self.vertices.count(v):
            return False
        self.vertices.append(v)
        filas = columnas = len(self.matriz)
        matriz_aux =[[None]*(filas+1) for i in range(columnas+1)]
        
        for f in range (filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[c][f] 
        self.matriz = matriz_aux
        return True
    
    def agregar_aristas(self, inicio, fin):
        if (self.esta_en_vertices(inicio)) and (self.esta_en_vertices(fin)):
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = 1
            self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = 1 
            return True
        else:
            print("Alguno de los vertices no se encuentra registrado")
    
    def verificar_arista(self,inicio,fin):
        if(self.esta_en_vertices(inicio) and self.esta_en_vertices(fin)):
            if((self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)]==1) and (self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] == 1)):
                print("Coincidencia encontrada")
                return True
        else: 
            print("No existen los vertices espcificados")
            return False

if _name_ == "_main_":
    g = Graph()

    iCantidad_vertices = int(input("Ingresar cantidad de vertices a utilizar:  "))
    for i in range (iCantidad_vertices):
        sNombre = str(input("Ingresar identificador del vertice:  "))
        g.agregar_vertices(sNombre)
    
    print ("MENÚ")
    print ("1) Agregar un vertice nuevo")
    print ("2) Agreagar arista")
    print ("3) Imprimir matriz")
    print ("4) Salir")
    
    
    
    while True:
        iOption = int(input("Elija una opción: "))
        if iOption == 1:
            sNombre = str(input("Ingresar identificador del vertice:  "))
            g.agregar_vertices(sNombre)
        elif iOption == 2:
            sInicio = str(input("Igresar el vertice de partida:  "))
            sFin = str(input("Ingresar vertice de llegada:  "))
            g.agregar_aristas(sInicio,sFin)
        elif iOption == 3:
            g.pintar_matriz(g.matriz,False)
        elif iOption == 4:
            break
        else:
            print("Opción no válida")