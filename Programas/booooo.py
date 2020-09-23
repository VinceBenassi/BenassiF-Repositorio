from random import randint, random

r = 8
t = 5
d = [3,4,2,5,True,["hello",23]]
s = ";"

def numeros(elegido,v=50): 
    print(elegido * v)

numeros("70")

buscador = 7
print(buscador in d)

print(s.join(d[5][0]))
print(d[5][0].replace, "hola")

print(len(d))

f = d[5][0]
print(f)

edad = 40

if edad >= 0 and edad <= 18:
    print("eres un niño")
elif edad >= 18 and edad <= 27:
    print("eres un joven")
elif edad >= 27 and edad <= 60:
    print("eres un adulto")
else:
    print("eres un viejo decrepito desagradecido y gritón")

for i in range(1):
    j = d[5][1] * d[2]
    print("el resultado es: "+ str(j))


while t <= r:
    t = t + 1
    print("Chuck Shurley es dios")


d[2] = 5
print(d[2])

ad = 0

while ad <= 10:
    ad = ad + 1
    print("El contador vale: ", ad)


print("hola, cual es su nombre?")
nombre = input("Escribe tu nombre:")
print("bienvenido a python", nombre)

edad = input("Introduce tu edad, por favor: ")
edad = int(edad)
if edad <= 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")



valor = randint(0,30)
print(valor)