# DataFrames
nombres = c("Franco", "Eliacer", "Josué", "Bárbara", "Maximiliano")
sexo = c("H", "H", "H", "M", "H")
edad = c(21, 20, 19, 24, 23)
nombres
sexo
edad

misDatos = data.frame(nombres, sexo, edad)
misDatos

str(misDatos)
names(misDatos)

# Acceso a Variables dentro de un DataFrame

# Primeros 3 datos del dataframe
misDatos[1:3,]

# Datos de la primera columna
misDatos[,1]
misDatos$nombres
misDatos[,"nombres"]
misDatos[["nombres"]]

# Media
mean(misDatos[,3])
mean(misDatos$edad)

# Subset (permite seleccionar una parte de un dataframe)
hombres = subset(misDatos, sexo == "H")
hombres

mujeres = subset(misDatos, sexo == "M")
mujeres

edades = subset(misDatos, edad >= 20)
edades

# rbind y merge (Métodos para unir dataframes con las mismas variables)
angeles = data.frame(nombre = c("Samael", "Ariel", "Amenadiel", "Castiel", "Gabriel", "Miguel"),
                     clase=c("Arcángel", "Ángel", "Ángel", "Ángel", "Arcángel", "Arcángel"))

angeles2 = data.frame(nombre = c("Rafael", "Uriel", "Remiel"), clase = c("Arcángel", "Ángel", "Ángel"))

angeles
angeles2

angeles3 = rbind(angeles, angeles2)
angeles3

angeles4 = merge(angeles, angeles2)
angeles4

#all = TRUE, all = false
# Registros mo repetidos
angeles5 = merge(angeles, angeles2, all = TRUE)
angeles5

angeles6 = merge(angeles, angeles2, all = FALSE)
angeles6
