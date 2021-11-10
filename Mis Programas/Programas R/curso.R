x = c(23, 45, 67, 54, 90, 100)
x
x[c(1,3)]
x[3:6]

y = c(5, 6)
y
length(y)
x[y]
x[-3: -5]

1:10
seq(10)
seq(6,20)
seq(6,20, by = 2)
seq(from=14, to=30, by=3)

repeticion = rep(8,4)
repeticion
rep(c(1,2,3,4), 4)
rep(seq(10), 3)

# Any para buscar un valor mayor, menor o igual a algo
listado = c(2, 10, 15, 20, 40, 60)
any(listado > 50)

# All para preguntar si todos los valores del
# vector son mayores, menores o iguales a algo
listado2 = seq(4)
all(listado2 < 0)

# NA es algo que no existe
e = c(65, NA, 34, 21, 154, 16)
e
mean(e)
mean(e, na.rm=T)

# NULL es algo vacío
f = c(65, NULL, 34, 21, 154, 16)
mean(f)

# Filtros
s = c(2, 6, 7, 9, 10, 15, 18)
filtrar = s[s*s > 8]
filtrar
s*s
s*s > 8

t = s[s*2 < 8]
t
s*2
s*2 < 8

lista = c(2, 1:4, NA, 20)
lista
lista[lista > 5]
subset(lista, lista > 5)

# Función which para mostrar la posición 
# de lo que se pide mostrando el indice
vector1 = c(2, 4, 5, 3, 7, 9, 14)
vector1
vector1*3 > 10
which(vector1*3 > 10)

# condicion if-else
ifelse(vector1 > 5, 5*vector1, 10*vector1)

num = 24
num2 = 30
ifelse(num > num2, "este numero si es mayor", "tu numero es menor a lo indicado")

# Funciones Utiles
a = (1:10)
a
min(a)
max(a)
sum(a)
sqrt(a)

ordenar = c(3, 6, 4, 2, 8, 2, 4, 7, 9, 1, 5)
ordenar
sort(ordenar)
unique(ordenar)
which.min(ordenar)
which.max(ordenar)

# Otros tipos de vectores
VT = c(T, F, T)
VT

valor = 40
valor > 50

vt2 = c(T, T, T, valor == 5)
vt2

fruta = c("Manzana", "Naranja", "Plátano", "Kiwi")
fruta
precios = c(1000, 500, 300, 700)
precios
names(precios) = fruta
precios