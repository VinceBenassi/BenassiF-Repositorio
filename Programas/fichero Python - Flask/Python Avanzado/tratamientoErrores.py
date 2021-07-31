# Tratando Errores

try:
    archivo = open("datos.txt", "w")
    archivo.write("Datos para el archivo")
    archivo.close()
except:
    print("Error... El archivo no existe!!!")
else:
    print("Archivo ejecutado correctamente")
finally:
    print("Archivo tratado a finalizado.")

print("Continuando el programa")

