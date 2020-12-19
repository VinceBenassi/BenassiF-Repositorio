# Programa de Franco Benassi
# Proyecto #4 y 5 Sistemas Inteligentes 2020
# Ejercicio 4
import math

Vector_A = [2,1,0,2,0,1,1,1]
Vector_B = [2,1,1,1,1,0,1,1]
Vector_P = [1,2,3,0,4,6,7,9]
Vector_Q = [2,4,3,1,8,2,4,1]
Vector_S = [2,1,4,7,1,4,5,6]
Vector_T = [3,3,3,6,1,1,7,8]

def DistanciaCoseno(A, B):
    Vector1 = A
    Vector2 = B

    numero = sum([Vector1[x] for x in range(len(A))])
    numero2 = sum([Vector2[i] for i in range(len(B))])
    numerador = numero * numero2

    denominador1 = sum([Vector1[x]**2 for x in range(len(A))])
    denominador2 = sum([Vector2[x]**2 for x in range(len(B))]) 
    denominador = math.sqrt(denominador1) * math.sqrt(denominador2)
 
    return float(numerador/denominador)

print("La medida de la distancia para los vectores A y B es de:", DistanciaCoseno(Vector_A, Vector_B))
print("La medida de distancia para los vectores P y Q es de:", DistanciaCoseno(Vector_P, Vector_Q))
print("La medida de distancia para los vectores S y T es de:", DistanciaCoseno(Vector_S, Vector_T), "\n")

def ConversionGrados(A):
    return float(A*(180/math.pi))

print("La distancia expresada en grados para los vectores A y B es de: " + str(ConversionGrados(DistanciaCoseno(Vector_A, Vector_B))) + "°")
print("La distancia expresada en grados para los vectores P y Q es de: " + str(ConversionGrados(DistanciaCoseno(Vector_P, Vector_Q))) + "°")
print("La distancia expresada en grados para los vectores S y T es de: " + str(ConversionGrados(DistanciaCoseno(Vector_S, Vector_T))) + "°")