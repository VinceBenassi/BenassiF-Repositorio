import cv2

def operacion(imagen):
    img = cv2.imread(imagen)
    gray_img = cv2.cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    moment = cv2.moments(gray_img)
    X = int(moment["m10"] / moment["m00"])
    Y = int(moment["m01"] / moment["m00"])
    cv2.circle(img, (X, Y), 15, (205, 114, 101), 1)
    cv2.imshow("Center of the Image", img)
    cv2.waitKey(0)

operacion('/home/franco/Documentos/Informática/Interfaces de Grafica de Usuario/Proyecto 1/a.png')