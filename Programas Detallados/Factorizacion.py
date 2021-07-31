# importamos libreria con la que se va a trabajar
import numpy as np

print('Descomposición A=LU, matrices cuadradas')
# creamos una variable en la que se almacenaran los valores ingresados por pantalla
m = int(input('Introduce el numero de filas: '))

# inicializamos la matriz original donde se almacenaran los coeficientes
# cabe resaltar que estara solo con ceros al principio
matriz = np.zeros([m,m])
# inicializamos la matriz L donde se almacenaran los coeficientes
# cabe resaltar que estara solo con ceros al principio
u = np.zeros([m,m])
# inicializamos la matriz U donde se almacenaran los coeficientes
# cabe resaltar que estara solo con ceros al principio
l = np.zeros([m,m])
print('Introduce los elementos de la matriz: ')

# mediante ciclos for controlaremos las operaciones que se aplicaran a
# las filas y las columnas 
for filas in range(0,m):
    for columnas in range(0,m):
# indicamos al usuario la poscición en la que introducira datos a la matriz
        matriz[filas,columnas] = (input('Elemento a [ ' + 'fila '+ str(filas + 1) + ',' + 'columna '+ str(columnas + 1) + ' ]=  '))
# nos aseguramos de trabajar con numeros flotantes especificandole a python
        matriz[filas,columnas] = float(matriz[filas,columnas])
# inicializamos la insercion de datos a la matriz U
        u[filas,columnas] = matriz[filas,columnas]

#operaciones para hacer ceros debajo de la diagonal principal
# k sera un contador de elemntos
for k in range(0,m):
# r sera la cantidad de renglones o filas
    for r in range(0,m):
# asignamos valores a la diagonal principal de la matriz L
        if (k == r):
            l[k, r] = 1
# aplicamos operaciones de la eliminacion gaussiana
        if (k < r):
            factor = (matriz[r,k]/matriz[k,k])
            l[r, k] = factor
# comenzamos a poner ceros en la matriz 
            for c in range(0,m):
                matriz[r,c] = matriz[r,c]-(factor*matriz[k,c])
                u[r,c] = matriz[r,c]

print('impresión de resultados: ')
print('Matriz L')
print(l)
print('------------------')
print('Matriz U')
print(u) 
print('------------------')

# comprobante de operación
# para saber si el resultado es correcto solo debemos volver a multiplicar la
# Matriz U por la Matriz L si el procedimiento esta bien echo 
# al ocupar el metodo dot() de numpy el resultado debera ser la matriz ingresada 
# por el usuario
a = np.dot(l,u)
print(a)
