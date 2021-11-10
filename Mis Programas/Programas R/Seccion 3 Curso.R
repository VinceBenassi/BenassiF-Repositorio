# Matrices
matriz = 1:9
matriz
# Dando dimensión a la matriz creando una matriz de 3x3
dim(matriz) = c(3,3)
matriz

# Segunda forma para hacer una matriz
# Ordenada por Columnas
matriz2 = matrix(5:20, nrow=4, ncol=4)
matriz2
# Asignando nombres a las filas
rownames(matriz2) = c("f1", "f2", "f3", "f4")
matriz2
# Ordenada por filas
matriz2 = matrix(5:20, nrow=4, ncol=4, byrow=TRUE)
matriz2

#Tercera forma para hacer una matriz
matriz3 = matrix(nrow=2, ncol=2)
matriz3
# Asignando valores
matriz3[1,1] = 40
matriz3[1,2] = 56
matriz3[2,1] = 3
matriz3

# Operaciones con Matrices
matriz4 = matrix(1:4, nrow=2, ncol=2)
matriz4

matriz5 = matrix(6:9, nrow=2, ncol=2)
matriz5

# Multiplicar Matrices
matriz4 %*% matriz5
matriz5 %*% matriz5

5 * matriz4
5 * matriz5

# Suma de Matrices
matriz4 + matriz5

# Resta de Matrices
matriz4 - matriz5

# Factores
paises = c("CHI", "MEX", "ARG", "USA")
paises

factorPaises = as.factor(paises)
factorPaises
table(factorPaises)

meses = c("Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")
cumpleaños = c("Mar", "Abr", "Abr", "Abr", "Jun", "Jul", "Ago", "Sep", "Dic", "Dic", "Dic")
meses
cumpleaños

factorCumpleaños = as.factor(cumpleaños)
factorCumpleaños
table(factorCumpleaños)

factorMeses = as.factor(meses)
factorMeses
table(factorMeses)

# Listas
nombres = list("Andrés", "Carla", "Eliacer", "Omar", 20, 19, 21, 19)
nombres

amigos = list(amigas = "Natalia", amigos = c("Juan", "Alvaro"))
amigos

# Acceso a Elementos de una Lista
empleados = list(empleado=c("Gabriel", "Pedro", "Diego"), salario=c(40000, 60000, 55000), edad=c(25, 27, 30))
empleados
empleados$salario[1]
empleados[["edad"]]
empleados$empleado[3]