import cv2
import numpy as np

img = cv2.imread('/home/francob/Documentos/Informática/Integración III/Phantom-Cyto-Seq/Seq/Img000038.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

contornos, jerarquia = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contornos, -1, (0, 255, 0), 3)

#for i in range(len(contornos)):
    #cv2.drawContours(img, contornos, i, (0, 255, 0), 3)
    #cv2.imshow("Imagen", img)
    #cv2.waitKey(0)

cv2.imshow("Imagen", img)
cv2.imshow("Imagen2", th)     
cv2.waitKey(0)
cv2.destroyAllWindows()