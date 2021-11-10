import cv2
import  numpy as np

imagen = cv2.imread('/home/francob/Documentos/Informática/Integración III/Phantom-Cyto-Seq/Seq/Img000038.jpg')
cv2.imshow('Original', imagen)

#convertir a grises
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', grises)

# detección de bordes
bordes = cv2.Canny(grises, 50, 150, apertureSize=3)
cv2.imshow('Bordes', bordes)

# HoughLines permite obtener el arreglo 2D requerido
# en la transformada de hough
# Parámetros: 1.- imagen que se le aplica la transformación
# 2.- resolución de distancia para el acumulador (r)
# 3.- resolución en ángulo para el acumulador (theta)
# 4.- umbral para conocer si se toma como linea lo analizado
# 5.- None para concluir, a veces si no se coloca esto al final
# la transformada devuelve un valor none y todo falla
lineas = cv2.HoughLines(bordes, 1, np.pi/180, 150, None)

if lineas is not None:
    for resultados in range(0, len(lineas)):
        rho = lineas[resultados][0][0] # Obtiene los valores de la distancia (rho)
        theta = lineas[resultados][0][1] # Obtiene los valores del ángulo (theta)
        guardarCosTheta = np.cos(theta)
        guardarSenTheta = np.sin(theta)
        gValorAcumuladorCosTheta = guardarCosTheta*rho
        gValorAcumuladorSenTheta = guardarSenTheta*rho

        # Se recorre todo de -1000 a 1000 pixeles
        x1 = int(gValorAcumuladorCosTheta + 1000*(-guardarSenTheta))
        y1 = int(gValorAcumuladorSenTheta + 1000*(guardarCosTheta))
        x2 = int(gValorAcumuladorCosTheta - 1000*(-guardarSenTheta))
        y2 = int(gValorAcumuladorSenTheta - 1000*(guardarCosTheta))

        # Mostrar los valores hallados
        print("({},{}) ({},{})".format(x1,y1, x2,y2))

        # Generar las líneas para montarlas en la imagen original
        cv2.line(imagen, (x1,y1), (x2,y2), (0,0,255), 2)

# Mostrar la imagen original con las
# lineas encontradas
cv2.imshow('Hough', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()