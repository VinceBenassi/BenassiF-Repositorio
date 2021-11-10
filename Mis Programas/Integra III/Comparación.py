import cv2 as cv
import numpy as np
import time

img = cv.imread("/home/francob/Documentos/Informática/Integración III/Phantom-Cyto-Seq/Seq/Img001070.jpg")
grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


def circulos(filterUse):
    airParticles = []
    start = time.time()
    detectedCircle = cv.HoughCircles(
        filterUse, cv.HOUGH_GRADIENT, 1, 2, param1=40, param2=15, minRadius=9, maxRadius=12)

    if detectedCircle is not None:
        detectedCircle = np.uint16(np.around(detectedCircle))

        for dC in detectedCircle[0, :]:
            cX = dC[0]
            cY = dC[1]
            r = dC[2]

            airParticles.append({'centroid': (cX, cY), 'radius': r})
            cv.circle(img, (cX, cY), r, (0, 255, 0), 2)
            cv.circle(img, (cX, cY), 1, (0, 255, 0), 3)
    end = time.time()
    print(end-start)
    print(len(airParticles))


cv.imshow("Original image", img)

blurFilter = cv.blur(grayScale, (5, 5))
circulos(blurFilter)
cv.imshow("Blur filter", img)
cv.waitKey(0)

medianBlur = cv.medianBlur(grayScale, 5)
circulos(medianBlur)
cv.imshow("Median blur filter", img)
cv.waitKey(0)

gaussianBlur = cv.GaussianBlur(grayScale, (5, 5), cv.BORDER_DEFAULT)
circulos(gaussianBlur)
cv.imshow("Gaussian Blur Filter", img)
cv.waitKey(0)

bilateralFilter = cv.bilateralFilter(grayScale, 5, 75, 75)
circulos(bilateralFilter)
cv.imshow("Bilateral filter", img)
cv.waitKey(0)

cv.destroyAllWindows()