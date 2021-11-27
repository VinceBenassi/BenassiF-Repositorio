import ply.lex as lex
import codecs
import os

palabrasReservadas = {
    "mai"       : "IF",
    "nu"        : "ELSE",
    "lelu"      : "WHILE",
    "pengeln"   : "PRINT",
    "ka"        : "AND",
    "kam"       : "OR",
    "kil"       : "NOT",
    "el"        : "FUNCION",
    "mew"       : "HASTA",
    "dewman"    : "THEN",
    "chi"       : "CAMBIO",
    "ñitholn"   : "BEGIN",
    "afn"       : "END",
    "ponwi"     : "IN",
    "pule"      : "FOR",
    "inau"      : "CONST"
}

tokens = [
    "COMA",
    "ASIGNACION",
    "ABRECORCHETE",
    "CIERRACORCHETE",
    "PUNTOCOMA",
    "LLAVEIZQ",
    "LLAVEDER",
    "PARENTESISIZQ",
    "PARENTESISDER",
    "DOBLEPUNTO",
    "IGUALQUE",
    "MAYORQUE",
    "MAYORIGUAL",
    "MENORQUE",
    "MENORIGUAL",
    "DISTINTO",
    "MAS",
    "MENOS",
    "POR",
    "OBELO",
    "DECIMAL",
    "ENTERO",
    "CADENA",
    "ID",
]+list(palabrasReservadas.values())

#Tokens
t_ignore         = "\t"

t_COMA           = r"\,"
t_ASIGNACION     = r"="
t_ABRECORCHETE   = r"\["
t_CIERRACORCHETE = r"\]"
t_PUNTOCOMA      = r";"
t_LLAVEIZQ       = r"{"
t_LLAVEDER       = r"}"
t_PARENTESISIZQ  = r"\("
t_PARENTESISDER  = r"\)"
t_DOBLEPUNTO     = r":"
t_IGUALQUE       = r"=="
t_DISTINTO       = r"!="
t_MAYORQUE       = r">"
t_MENORQUE       = r"<"
t_MAYORIGUAL     = r">="
t_MENORIGUAL     = r"<="
t_MAS            = r"\+"
t_MENOS          = r"-"
t_POR            = r"\*"
t_OBELO          = r"/"
t_IF             = r"mai"
t_WHILE          = r"lelu"
t_PRINT          = r"pengeln"
t_AND            = r"ka"
t_OR             = r"kam"
t_NOT            = r"kil"
t_FUNCION        = r"el"
t_THEN           = r"dewman"
t_HASTA          = r"mew"
t_CAMBIO         = r"chi"
    
def t_newLine(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r"\#.*"
    pass

def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = palabrasReservadas.get(t.value.lower(),"ID")
    return t

def t_ENTERO(t):
    r"\d+"
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d",t.value)
        t.value = 0
    return t

def t_DECIMAL(t):
    r"(\d*\.\d+)|(\d+\.\d*)"
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor flotante demasiado largo %d",t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r"\'.*?\'"
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("Caracter invalido '%s'" %t.value[0])
    t.lexer.skip(1)

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

analizador = lex.lex()
analizador.input(cadena)

while True:
    tokenMomentaneo = analizador.token()
    if not tokenMomentaneo : break
    print(tokenMomentaneo)
