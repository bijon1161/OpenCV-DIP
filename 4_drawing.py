import cv2 as cv
import numpy as np

canvas = np.zeros((300,300,3),dtype="uint8")

def display(winname,image):
    cv.imshow(winname,image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# red = (0,0,255)
# green = (0,255,0)
# blue= (255,0,0)

# cv.line(canvas,(0,0),(300,300),green,2)
# cv.line(canvas,(300,0),(0,300),red,3)

# cv.rectangle(canvas,(60,60),(200,200),blue,5)
centerx,centery = (canvas.shape[1]//2,canvas.shape[0]//2)
white =(255,255,255)
for r in range(0,175,25):
    cv.circle(canvas,(centerx,centery),r,white)

display("circles",canvas)