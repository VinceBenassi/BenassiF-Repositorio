import ply.yacc as yacc
import os
import codecs
from analizadorLexico import tokens, analizador
from sys import stdin

# precedencia para evitar errores en el analizador
precedencia = (
    ('derecha', 'BEGIN', 'IF', 'WHILE'),
    ('derecha', 'ASIGNACION'),
    ('derecha', 'IGUALQUE'),
    ('izquierda', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL'),
    ('izquierda', 'MAS', 'MENOS'),
    ('izquierda', 'POR', 'OBELO'),
    ('izquierda', 'PARENTESISIZQ', 'PARENTESISDER'),
    ('izquierda', 'LLAVEIZQ', 'LLAVEDER')
)

nombres = {}

def produccion_programa(p):
    '''program: instrucciones'''
    print("program")
    p[0] = p[1]
    
def produccion_instrucciones_lista(p):
    '''instrucciones: instrucciones instruccion'''
    p[1].append(p[2])
    p[0] = p[1]
    print("instrucciones lista")
    
def produccion_instrucciones_instruccion(p):
    '''instrucciones: instruccion'''
    p[0] = [p[1]]
    
def produccion_instruccion(p):
    '''instruccion: imprimir_instr
                    | asignacion_instr
                    | if_instr
                    | while_instr'''
    p[0] = p[1]
    
def produccion_if(p):
    '''if_instr: IF PARENTESISIZQ expresion_logica PARENTESISDER LLAVEIZQ statement LLAVEDER'''
    print(p[3])
    if(p[3]):
        p[0] = p[6]
        
def produccion_statement(p):
    '''statement: imprimir_instr
                    | if_instr
                    | expresion
                    | while_instr'''
    p[0] = p[1]
    print(p[0])
    
def produccion_while(p):
    '''while_instr: WHILE PARENTESISIZQ expresion_logica PARENTESISDER LLAVEIZQ statement LLAVEDER'''
    while(p[3]):
        p[0] = p[6]
        
def produccion_asignacion(p):
    '''asignacion_instr: ID IGUAL expresion PUNTOCOMA'''
    nombres[p[1]] = p[3]

def produccion_asignacion_tipo(p):
    '''expresion: ENTERO
                | DECIMAL
                | CADENA'''
    p[0] = p[1]
    
def produccion_expresion_id(p):
    '''expresion: ID'''
    p[0] = nombres[p[1]]
    
# Funciones del Lenguaje
def produccion_print(p):
    '''imprimir_instr: PRINT PARENTESISIZQ expresion PARENTESISDER PUNTOCOMA'''
    p[0] = p[3]

def produccion_expresion_group(p):
    '''expresion: PARENTESISIZQ expresion PARENTESISDER'''
    p[0] = p[2]

def produccion_expresion_logica(p):
    '''expresion_logica: expresion MENORQUE expresion
                        | expresion MAYORQUE expresion
                        | expresion IGUALQUE expresion
                        | expresion DISTINTO expresion
                        | expresion MAYORIGUAL expresion
                        | expresion MENORIGUAL expresion'''
    if   p[2] == '<': p[0] = p[1] < p[3]
    elif p[2] == '>': p[0] = p[1] > p[3]
    elif p[2] == '==': p[0] = p[1] == p[3]
    elif p[2] == '!=': p[0] = p[1] != p[3]
    elif p[2] == '<=': p[0] = p[1] <= p[3]
    elif p[2] == '>=': p[0] = p[1] >= p[3]
    
def produccion_expresion_logica_group(p):
    '''expresion_logica: PARENTESISIZQ expresion_logica PARENTESISDER'''
    p[0] = p[2]
    
def produccion_expresion_logica_group(p):
    '''expresion_logica: PARENTESISIZQ expresion_logica PARENTESISDER MENORQUE PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER MAYORQUE PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER IGUALQUE PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER DISTINTO PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER MAYORIGUAL PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER MENORIGUAL PARENTESISIZQ expresion_logica PARENTESISDER'''
    if   p[4] == '<': p[0] = p[2] < p[5]
    elif p[4] == '>': p[0] = p[2] > p[5]
    elif p[4] == '==': p[0] = p[2] == p[5]
    elif p[4] == '!=': p[0] = p[2] != p[5]
    elif p[2] == '<=': p[0] = p[2] <= p[5]
    elif p[2] == '>=': p[0] = p[2] >= p[5]
    
def produccion_expresion_operador_logico(p):
    '''expresion_logica: PARENTESISIZQ expresion_logica PARENTESISDER AND PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER OR PARENTESISIZQ expresion_logica PARENTESISDER
                        | PARENTESISIZQ expresion_logica PARENTESISDER NOT PARENTESISIZQ expresion_logica PARENTESISDER'''
    if p[4] == 'ka': p[0] = p[2] and p[5]
    if p[4] == 'kam': p[0] = p[2] or p[5]
    if p[4] == 'kil': p[0] = p[2] is not p[5]
    
def produccion_expresion_operaciones(p):
    '''expresion: expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion OBELO expresion'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
        
def produccion_error(p):
    print("Error de sintaxis", p)
    print("Error en la línea"+ str(p.lineno))
    
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    contador = 1
    
    for base, dirs, archivos in os.walk(directorio):
        ficheros.append(archivos)
        
    for file in archivos:
        print(str(contador) + ". " + file)
        contador += 1
        
    while respuesta == False:
        numArchivo = input('\nNúmero de la prueba: ')
        for file in archivos:
            if file == archivos[int(numArchivo)-1]:
                respuesta = True
                break
            
    print("Has elegido \"%s\" \n" %archivos[int(numArchivo)-1])
    
    return archivos[int(numArchivo)-1]

# se crea un directorio para hacer las pruebas
directorio = '/home/francob/Documentos/Mis Programas Locales/Computación/Compilador 2/prueba/'
archivo = buscarFicheros(directorio)
prueba = directorio+archivo

#Imprime registro lexico
archivo = codecs.open(prueba,"r","utf-8")
cadena = archivo.read()
archivo.close()

# Variable para manejar el yacc que permite al programa
# hacer un análisis sintáctico de todo el código fuente 
parser = yacc.yacc()
resultado = parser.parse(cadena)
print(resultado)