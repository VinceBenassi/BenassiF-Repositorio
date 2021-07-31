# Convirtiendo en caricatura una imagen
# Por Franco Benassi
import cv2

# Carga la imagen
img = cv2.imread("/home/francob/Imágenes/loki.jpg")

# Bordes
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur(gris, 5)
bordes = cv2.adaptiveThreshold(gris, 255, 
         cv2.ADAPTIVE_THRESH_MEAN_C, 
         cv2.THRESH_BINARY, 9, 9)

# Volviendo Caricatura
color = cv2.bilateralFilter(img, 9, 250, 250)
caricatura = cv2.bitwise_and(color, color, mask=bordes)

cv2.imshow("Imagen", img)
cv2.imshow("Bordes", bordes)
cv2.imshow("Caricatura", caricatura)
cv2.waitKey(0)
cv2.destroyAllWindows()