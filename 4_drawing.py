import cv2 as cv
import numpy as np

canvas = np.zeros((300,300,3),dtype="uint8")

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()


for i in range(0,25):
    radius = np.random.randint(5,200)
    color = np.random.randint(0,256,size=(3,)).tolist()
    pt = np.random.randint(0,300,size=(2,))

    cv.circle(canvas,tuple(pt),radius,color,-1)

display("canvas",canvas)
cv.imwrite('./images/Canvas.png',canvas)