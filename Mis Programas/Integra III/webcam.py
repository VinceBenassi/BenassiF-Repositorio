import numpy
import cv2 as cv

def camaraWeb():
    captura = cv.VideoCapture(0)

    while True:
        ret, frame = captura.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        cv.imshow('fotograma', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv.destroyAllWindows()

camaraWeb()

#def cargarVideo():
    #captura = cv.VideoCapture()