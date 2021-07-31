# Expresiones Regulares
import re

texto = "Las decisiones difíciles requieren voluntades fuertes"

def buscarCoincidencia(patron):
    coincidencia = re.search(patron, texto)
    resultado = re.findall(patron, texto)
    print(resultado)

    veces = len(resultado)
    print(veces)

    if coincidencia:
        print("Se ha encontrado la palabra", patron, "en el texto")
        posicionInicial = coincidencia.start()
        posicionFinal = coincidencia.end()
        print("La palabra", patron, "empieza en la posición", posicionInicial, "y termina en la", posicionFinal)
    else:
        print("No se ha encontrado la palabra", patron, "como coincidencia")

#final = buscarCoincidencia("fuertes")