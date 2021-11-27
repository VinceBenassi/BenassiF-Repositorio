from enum import Enum

class Simbolo():
    def __init__(self, id, tipo, valor):
        self.id = id
        self.tipo = tipo
        self.valor = valor

simbolos = {}

def agregarSimbolo(simbolo):
    simbolos[simbolo.id] = simbolo

def obtenerSimbolo(id):
    if not id in simbolos:
        print('Error: variable', id, 'indefinida')
    
    return simbolos[id]

def actualizarSimbolo(simbolo):
    if not simbolo.id in simbolos:
        print('Error: variable', simbolo.id, 'indefinida')
    else:
        simbolos[simbolo.id] = simbolo